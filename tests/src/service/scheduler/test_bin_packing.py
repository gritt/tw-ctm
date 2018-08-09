import unittest

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


if __name__ == '__main__':
    unittest.main()
