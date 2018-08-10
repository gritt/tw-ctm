from src.entity.shift import Shift
from src.entity.track import Track
from src.service.scheduler.bin_packing import BinPacking

__author__ = 'gritt'


class Scheduler:
    # from 9 am till 12 noon
    MORNING_SHIFT = 180

    # from 13 pm till 17 pm
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

            except Exception as ex:

                # when there's no best fit for the remaining time, open a new shift
                self.shifts.append(current_shift)

                current_shift = 0

                # follow sequence for morning > afternoon > morning.. due to shift sizes
                current_shift_option = 1 if current_shift_option == 0 else 0
                continue

        # unclosed shift (has remaining time) also must be added
        if current_shift != 0:
            self.shifts.append(current_shift)

        return self.shifts

    def _new_shift(self, option):

        current_shift = Shift()
        current_shift.set_minutes(self.shift_options[option])

        if self.shift_options[option] == self.MORNING_SHIFT:
            current_shift.set_start_time(9)
            current_shift.set_end_time(12)

        if self.shift_options[option] == self.AFTERNOON_SHIFT:
            current_shift.set_start_time(13)
            current_shift.set_end_time(17)

        return current_shift

    def _process_tracks(self):

        # starts with a morning shift
        current_shift_option = 0
        current_track_day = 1
        current_track = 0

        while len(self.shifts) > 0:

            try:

                index = 0
                for shift in self.shifts:

                    if current_track == 0:
                        current_track = Track()
                        current_track.set_day(current_track_day)
                        current_track.set_shifts_limit(len(self.shift_options))

                    # matched a needed shift (same time), must start with a morning shift
                    if shift.get_minutes() == self.shift_options[current_shift_option]:

                        # adds the current shift in the track
                        current_track.add_shift(shift)
                        # remove shift from available ones
                        self.shifts.pop(index)

                        # close this track, completed
                        if current_track.shifts_limit == len(current_track.shifts):
                            # saves the current track which has been completed
                            self.tracks.append(current_track)
                            current_track = 0
                            current_track_day += 1

                        # next shift must be opposite
                        if current_shift_option == 0:
                            current_shift_option = 1
                            index += 1
                            continue
                        if current_shift_option == 1:
                            current_shift_option = 0
                            index += 1
                            continue

                    index += 1

            except Exception as ex:
                # saves the current track which has been completed
                self.tracks.append(current_track)

                # resets so a new track will be created
                current_track = 0
                current_track_day += 1

        # unclosed track (has remaining shift(s)) also must be added
        if current_track != 0:
            if len(current_track.shifts) > 0:
                self.tracks.append(current_track)

        return self.tracks
