__author__ = 'gritt'


class Talk:

    def __init__(self):
        self._name = ''
        self._duration = 0
        self._starting_time = ''
        self._ending_time = ''

    def set_name(self, name):
        self._name = name
        return self

    def set_duration(self, duration):
        self._duration = duration

    def set_starting_time(self, starting_time):
        self._starting_time = starting_time

    def set_ending_time(self, ending_time):
        self._ending_time = ending_time

    def get_name(self):
        return self._name

    def get_duration(self):
        return self._duration

    def get_starting_time(self):
        return self._starting_time

    def get_ending_time(self):
        return self._ending_time
