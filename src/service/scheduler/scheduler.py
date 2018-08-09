from src.entity.shift import Shift
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

        # self.total_time = 0
        # self.shifts_number = 0

        # self.tracks = []
        self.shifts = []
        self.talks = []

    def schedule(self, talks):
        self.talks = talks
        self._process_shifts()

    def _process_shifts(self):

        # whether the current shift is morning or afternoon, which defines the bin size
        # every time  bin is closed, the next bin must be with the next shift (circularly)
        current_shift_option = 0

        # the current "bin" and it's packages (talks)
        current_shift = 0

        while len(self.talks) > 0:

            try:
                # first iteration, and shifts opening iterations
                if current_shift == 0:
                    current_shift = Shift()
                    current_shift.set_minutes(
                        self.shift_options[current_shift_option]
                    )

                # find a talk that bests fits in the remaining time
                best_fitted_index = self.bin_packing.get_best_fitting_talk(
                    current_shift.get_remaining_minutes(),
                    self.talks
                )

                # schedule the better fitted talk in the shift
                current_shift.add_talk(self.talks[best_fitted_index])

                # remove talk scheduled
                self.talks.pop(best_fitted_index)

            except Exception as ex:

                # when there no best fit for the remaining time, open a new shift
                self.shifts.append(current_shift)

                current_shift = 0

                # follow sequence for morning > afternoon > morning.. for due to shift sizes
                if current_shift_option == 0:
                    current_shift_option = 1
                    continue
                if current_shift_option == 1:
                    current_shift_option = 0
                    continue

        # unclosed shift (unprocessed remaining time) also must be added
        if current_shift != 0:
            self.shifts.append(current_shift)

        return self.shifts
