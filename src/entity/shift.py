__author__ = 'gritt'


class Shift:

    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.minutes = 0
        self.remaining_minutes = 0
        self.talks = []

    def set_start_time(self, start_time):
        self.start_time = start_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def set_minutes(self, minutes):
        self.minutes = minutes
        self.remaining_minutes = minutes

    def add_talk(self, talk):
        if self.remaining_minutes < talk.get_duration():
            raise Exception("Error: this talk does not fit in this shift")

        self.remaining_minutes -= talk.get_duration()
        self.talks.append(talk)

    # TODO @gritt, link a gap within talk's indices, so that the gap can be printed in the proper position in the schedule
    def add_interval(self, interval):
        if self.remaining_minutes < interval.get_duration():
            raise Exception("Error: this interval does not fit in this shift")

        self.remaining_minutes -= interval.get_duration()

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_minutes(self):
        return self.minutes

    def get_remaining_minutes(self):
        return self.remaining_minutes
