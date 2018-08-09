__author__ = 'gritt'


class Shift:

    def __init__(self):
        self.start_time = 0
        self.end_time = 0

        self.minutes = 0
        self.remaining_minutes = 0

        self.talks = []

    def set_minutes(self, minutes):
        self.minutes = minutes
        self.remaining_minutes = minutes

    def get_minutes(self):
        return self.minutes

    def get_remaining_minutes(self):
        return self.remaining_minutes

    def add_talk(self, talk):
        if self.remaining_minutes < talk.get_duration():
            raise Exception("Error: this talk does not fit in this shift")

        self.remaining_minutes -= talk.get_duration()
        self.talks.append(talk)
