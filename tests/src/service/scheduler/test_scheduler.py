import unittest

from src.entity.shift import Shift
from src.entity.talk import Talk
from src.service.scheduler.scheduler import Scheduler


class SchedulerTestCase(unittest.TestCase):

    def setUp(self):
        self.scheduler = Scheduler()

    def test_process_shifts_spliting(self):
        talk1 = Talk()
        talk1.set_duration(80)
        talk1.set_name("A")

        talk2 = Talk()
        talk2.set_duration(60)
        talk2.set_name("B")

        talk4 = Talk()
        talk4.set_duration(40)
        talk4.set_name("D")

        talk3 = Talk()
        talk3.set_duration(50)
        talk3.set_name("C")

        talk5 = Talk()
        talk5.set_duration(30)
        talk5.set_name("X")

        talk6 = Talk()
        talk6.set_duration(30)
        talk6.set_name("Y")

        talk7 = Talk()
        talk7.set_duration(30)
        talk7.set_name("Z")

        talks = []
        talks.append(talk1)
        talks.append(talk2)
        talks.append(talk3)
        talks.append(talk4)
        talks.append(talk5)
        talks.append(talk6)
        talks.append(talk7)

        self.scheduler.talks = talks

        shifts = self.scheduler._process_shifts()

        self.assertEquals(2, len(shifts))

        self.assertEquals(
            shifts[0].get_minutes(), 180
        )

        self.assertEquals(
            shifts[0].get_remaining_minutes(), 0
        )

        print shifts[1]

        self.assertEquals(
            shifts[1].get_minutes(), 240
        )

        self.assertEquals(
            shifts[1].get_remaining_minutes(), 100
        )

        self.assertEquals(
            shifts[0].talks[0].get_name(), "A"
        )

        self.assertEquals(
            shifts[1].talks[0].get_name(), "C"
        )

    def test_process_tracks(self):
        shift1 = Shift()
        shift1.set_minutes(180)

        shift2 = Shift()
        shift2.set_minutes(240)

        shift3 = Shift()
        shift3.set_minutes(240)

        shift4 = Shift()
        shift4.set_minutes(180)

        shift5 = Shift()
        shift5.set_minutes(180)

        shifts = []
        shifts.append(shift1)
        shifts.append(shift2)
        shifts.append(shift3)
        shifts.append(shift4)
        shifts.append(shift5)

        self.scheduler.shifts = shifts
        tracks = self.scheduler._process_tracks()

        # 3 days
        self.assertEquals(3, len(tracks))

    def test_process_tracks_one_day(self):
        shift1 = Shift()
        shift1.set_minutes(180)

        shift2 = Shift()
        shift2.set_minutes(240)

        shifts = []
        shifts.append(shift1)
        shifts.append(shift2)

        self.scheduler.shifts = shifts
        tracks = self.scheduler._process_tracks()

        # 1 days
        self.assertEquals(1, len(tracks))

    def test_process_tracks_one_day_and_half(self):
        shift1 = Shift()
        shift1.set_minutes(180)

        shift2 = Shift()
        shift2.set_minutes(240)

        shift3 = Shift()
        shift3.set_minutes(180)

        shifts = []
        shifts.append(shift1)
        shifts.append(shift2)
        shifts.append(shift3)

        self.scheduler.shifts = shifts
        tracks = self.scheduler._process_tracks()

        # 1 days
        self.assertEquals(2, len(tracks))

    def test_process_tracks_two_days(self):
        shift1 = Shift()
        shift1.set_minutes(180)

        shift2 = Shift()
        shift2.set_minutes(240)

        shift3 = Shift()
        shift3.set_minutes(240)

        shift4 = Shift()
        shift4.set_minutes(180)

        shifts = []
        shifts.append(shift1)
        shifts.append(shift2)
        shifts.append(shift3)
        shifts.append(shift4)

        self.scheduler.shifts = shifts
        tracks = self.scheduler._process_tracks()

        # 2 days
        self.assertEquals(2, len(tracks))

    def test_process_tracks_two_days_and_half(self):
        shift1 = Shift()
        shift1.set_minutes(180)

        shift2 = Shift()
        shift2.set_minutes(240)

        shift3 = Shift()
        shift3.set_minutes(240)

        shift4 = Shift()
        shift4.set_minutes(180)

        shift5 = Shift()
        shift5.set_minutes(180)

        shifts = []
        shifts.append(shift1)
        shifts.append(shift2)
        shifts.append(shift3)
        shifts.append(shift4)
        shifts.append(shift5)

        self.scheduler.shifts = shifts
        tracks = self.scheduler._process_tracks()

        # 3 days
        self.assertEquals(3, len(tracks))

    def test_process_tracks_four_days_and_half(self):
        shift1 = Shift()
        shift1.set_minutes(180)

        shift2 = Shift()
        shift2.set_minutes(240)

        shift3 = Shift()
        shift3.set_minutes(240)

        shift4 = Shift()
        shift4.set_minutes(180)

        shift6 = Shift()
        shift6.set_minutes(180)

        shift5 = Shift()
        shift5.set_minutes(240)

        shift7 = Shift()
        shift7.set_minutes(180)

        shifts = []
        shifts.append(shift1)
        shifts.append(shift2)
        shifts.append(shift3)
        shifts.append(shift4)
        shifts.append(shift5)
        shifts.append(shift6)
        shifts.append(shift7)

        self.scheduler.shifts = shifts
        tracks = self.scheduler._process_tracks()

        # 4 days
        self.assertEquals(4, len(tracks))


if __name__ == '__main__':
    unittest.main()
