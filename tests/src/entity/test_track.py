import unittest

from src.entity.shift import Shift
from src.entity.track import Track


class TrackTestCase(unittest.TestCase):

    @unittest.expectedFailure
    def test_add_shift_limit_failure(self):
        track = Track()
        track.set_day(1)
        track.set_shifts_limit(2)

        track.add_shift(Shift())
        track.add_shift(Shift())
        track.add_shift(Shift())


if __name__ == '__main__':
    unittest.main()
