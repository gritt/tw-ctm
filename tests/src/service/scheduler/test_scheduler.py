import unittest

from src.entity.talk import Talk
from src.service.scheduler.scheduler import Scheduler


class SchedulerTestCase(unittest.TestCase):

    def setUp(self):
        self.scheduler = Scheduler()

    def test_calculate_total_time(self):
        talks = []

        talk1 = Talk()
        talk1.set_duration(10)

        talks.append(talk1)

        self.scheduler.set_talks(talks)
        self.assertEquals(
            self.scheduler._calculate_total_time(), 10
        )

        talk2 = Talk()
        talk2.set_duration(10)
        talks.append(talk2)

        self.scheduler.set_talks(talks)
        self.assertEquals(
            self.scheduler._calculate_total_time(), 20
        )

        talk3 = Talk()
        talk3.set_duration(50)
        talks.append(talk3)

        self.scheduler.set_talks(talks)
        self.assertEquals(
            self.scheduler._calculate_total_time(), 70
        )


if __name__ == '__main__':
    unittest.main()
