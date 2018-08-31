__author__ = 'gritt'


class Interval:

    def __init__(self):
        self._duration = 0
        self._starting_time = ''
        self._ending_time = ''

    def set_duration(self, duration):
        self._duration = duration

    def get_duration(self):
        return self._duration
