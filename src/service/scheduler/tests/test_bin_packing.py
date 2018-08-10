import unittest

from src.entity.talk import Talk
from src.service.scheduler.bin_packing import BinPacking


class BinPackingTestCase(unittest.TestCase):

    def setUp(self):
        self.bin_packing = BinPacking()

    def test_calculate_fittingness(self):
        self.assertEquals(
            98, self.bin_packing._calculate_fittingness(100, 98)
        )
        self.assertEquals(
            95, self.bin_packing._calculate_fittingness(130, 124)
        )

        self.assertEquals(
            100, self.bin_packing._calculate_fittingness(280, 280)
        )

    @unittest.expectedFailure
    def test_calculate_fittingness_failure(self):
        self.bin_packing._calculate_fittingness(130, 150)

    def test_get_best_fitting_talk(self):
        talks = []

        talk1 = Talk()
        talk1.set_duration(45)

        talk2 = Talk()
        talk2.set_duration(38)

        talk3 = Talk()
        talk3.set_duration(64)

        talk4 = Talk()
        talk4.set_duration(54)

        talks.append(talk1)
        talks.append(talk2)
        talks.append(talk3)
        talks.append(talk4)

        remaining_bin_size = 60

        self.assertEquals(
            3,
            self.bin_packing.get_best_fitting_talk(remaining_bin_size, talks)
        )

    def test_get_best_fitting_talk_loop(self):
        talks = []

        talk1 = Talk()
        talk1.set_duration(35)

        talk2 = Talk()
        talk2.set_duration(30)

        talk3 = Talk()
        talk3.set_duration(40)

        talks.append(talk1)
        talks.append(talk2)
        talks.append(talk3)

        remaining_bin_size = 85

        self.assertEquals(
            2,
            self.bin_packing.get_best_fitting_talk(remaining_bin_size, talks)
        )

        talks.pop(2)
        remaining_bin_size = 85 - 40

        self.assertEquals(
            0,
            self.bin_packing.get_best_fitting_talk(remaining_bin_size, talks)
        )

    @unittest.expectedFailure
    def test_get_best_fitting_talk_failure(self):
        talks = []

        talk1 = Talk()
        talk1.set_duration(80)

        talk2 = Talk()
        talk2.set_duration(98)

        talks.append(talk1)
        talks.append(talk2)

        remaining_bin_size = 79

        self.bin_packing.get_best_fitting_talk(remaining_bin_size, talks)


if __name__ == '__main__':
    unittest.main()
