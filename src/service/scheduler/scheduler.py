__author__ = 'gritt'


class Scheduler:
    # from 9 am till 12 noon
    MORNING_SHIFT = 180
    # form 13 pm till 17 pm
    AFTERNOON_SHIFT = 240

    def __init__(self):
        self.total_time = 0
        self.shifts_number = 0

        self.tracks = []
        self.shifts = []
        self.talks = []

    def set_talks(self, talks):
        self.talks = talks

    def schedule(self, talks):
        self.talks = talks

        self._calculate_total_time()

        print self.total_time
        print self.talks

        self._calculate_number_of_shifts()

    def _calculate_total_time(self):
        time = 0
        for talk in self.talks:
            time += talk.get_duration()

        self.total_time = time

        return self.total_time

    def _calculate_number_of_shifts(self):
        print self.talks
