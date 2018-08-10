from src.entity.shift import Shift
from src.entity.track import Track
from src.service.scheduler.bin_packing import BinPacking

__author__ = 'gritt'


class Scheduler:
    # minutes from 9am to 12 noon
    MORNING_SHIFT = 180

    # minutes from 13pm to 17 pm
    AFTERNOON_SHIFT = 240

    def __init__(self):

        self.bin_packing = BinPacking()

        # the shifts of each track, or, day, are considered dynamically sized bins
        # the order to add new bins follows the order of the following list
        self.shift_options = [
            self.MORNING_SHIFT,
            self.AFTERNOON_SHIFT
        ]

        self.tracks = []
        self.shifts = []
        self.talks = []

    def schedule(self, talks):

        self.talks = talks
        self._process_shifts()
        self._process_tracks()

        return self.tracks

    # spread talks into shifts of different sizes (morning, afternoon)
    def _process_shifts(self):

        # the shift defines the "bin" size
        # talks are the package

        # every track (day) starts in the morning
        # a sequence must be followed when a new shift is required (morning -> afternoon -> morning..)

        current_shift_option = 0
        current_shift = 0

        while len(self.talks) > 0:
            try:

                # creates a new shift when there's none open
                if current_shift == 0:
                    current_shift = self._new_shift(current_shift_option)

                # find a talk that bests fits the remaining time available in the shift
                best_fitted_index = self.bin_packing.get_best_fitting_talk(
                    current_shift.get_remaining_minutes(),
                    self.talks
                )

                # schedule the better fitted talk
                current_shift.add_talk(self.talks[best_fitted_index])

                # remove from 'processing' list
                self.talks.pop(best_fitted_index)

            except Exception:
                # when there are no talks that best fit in the remaining time
                # closed the current shift and open a new one following the sequence for sizes

                self.shifts.append(current_shift)
                current_shift = 0
                current_shift_option = 1 if current_shift_option == 0 else 0
                continue

        # unclosed shift also must be added
        if current_shift != 0:
            self.shifts.append(current_shift)

        return self.shifts

    def _new_shift(self, option):

        shift = Shift()
        shift.set_minutes(self.shift_options[option])

        if self.shift_options[option] == self.MORNING_SHIFT:
            shift.set_start_time(9)
            shift.set_end_time(12)

        if self.shift_options[option] == self.AFTERNOON_SHIFT:
            shift.set_start_time(13)
            shift.set_end_time(17)

        return shift

    # spread shifts into tracks (days) always starting tracks with a morning shift
    def _process_tracks(self):

        current_shift_option = 0
        current_track_day = 1
        current_track = 0

        while len(self.shifts) > 0:
            try:
                index = 0
                for shift in self.shifts:

                    # creates a new track when there's none open
                    if current_track == 0:
                        current_track = Track()
                        current_track.set_day(current_track_day)
                        current_track.set_shifts_limit(len(self.shift_options))

                    # add shifts to a track when it matches the required option
                    # (first morning, than afternoon..)
                    if shift.get_minutes() == self.shift_options[current_shift_option]:

                        current_track.add_shift(shift)
                        self.shifts.pop(index)

                        # close this track, if all shifts are added
                        if current_track.shifts_limit == len(current_track.shifts):
                            self.tracks.append(current_track)
                            current_track = 0
                            current_track_day += 1

                        # next shift must be opposite
                        current_shift_option = 1 if current_shift_option == 0 else 0
                        index += 1
                        continue

                    index += 1

            except Exception:
                # when there space left in the track for more shifts
                # close the current track and reset for a new one
                self.tracks.append(current_track)
                current_track = 0
                current_track_day += 1

        # unclosed track (might have one shift) also must be added
        if current_track != 0:
            if len(current_track.shifts) > 0:
                self.tracks.append(current_track)

        return self.tracks
