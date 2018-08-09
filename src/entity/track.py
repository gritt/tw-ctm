__author__ = 'gritt'


class Track:

    def __init__(self):
        self.day = 0
        self.shifts = []
        self.shifts_limit = 0

    def set_day(self, day):
        self.day = day

    def get_day(self):
        return self.day

    def set_shifts_limit(self, limit):
        self.shifts_limit = limit

    def add_shift(self, shift):
        if len(self.shifts) == self.shifts_limit:
            raise Exception("Error: reached the max amount of shifts for this track")

        self.shifts.append(shift)

    def get_shifts(self):
        return self.shifts
