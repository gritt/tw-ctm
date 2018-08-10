from StringIO import StringIO
import datetime
import unittest
import sys

from src.entity.shift import Shift
from src.entity.talk import Talk
from src.service.io.track_writer import TrackWriter


class TrackWriterTestCase(unittest.TestCase):

    def setUp(self):
        self.track_writer = TrackWriter()
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_print_talk(self):
        talk = Talk()
        talk.set_name("Hello World")
        talk.set_duration(30)

        timer = datetime.timedelta(hours=9, minutes=00)

        self.track_writer._print_talk(talk, timer),
        self.assertEquals(sys.stdout.getvalue().strip(), "09:00AM Hello World 30min")

    def test_print_shift_end_afternoon(self):
        shift = Shift()
        shift.set_end_time(17)
        self.track_writer._print_shift_end(shift)
        self.assertEquals(sys.stdout.getvalue(), "05:00PM Networking Event\n")

    def test_print_shift_end_lunch(self):
        shift1 = Shift()
        shift1.set_end_time(12)
        self.track_writer._print_shift_end(shift1)
        self.assertEquals(sys.stdout.getvalue(), "12:00PM Lunch\n")


if __name__ == '__main__':
    unittest.main()
