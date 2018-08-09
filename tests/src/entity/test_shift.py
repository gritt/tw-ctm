import unittest

from src.entity.shift import Shift
from src.entity.talk import Talk


class ShiftTestCase(unittest.TestCase):

    def test_set_minutes(self):
        shift = Shift()
        shift.set_minutes(150)

        self.assertEquals(
            shift.get_remaining_minutes(), shift.minutes
        )

    def test_get_remaining_minutes(self):
        shift = Shift()
        shift.set_minutes(150)

        talk1 = Talk()
        talk1.set_duration(65)

        talk2 = Talk()
        talk2.set_duration(60)

        self.assertEquals(150, shift.get_remaining_minutes())

        shift.add_talk(talk1)
        self.assertEquals(85, shift.get_remaining_minutes())

        shift.add_talk(talk2)
        self.assertEquals(25, shift.get_remaining_minutes())

    def test_add_talk(self):
        shift = Shift()
        shift.set_minutes(150)

        talk1 = Talk()
        talk1.set_duration(65)
        talk1.set_name("A")

        talk2 = Talk()
        talk2.set_duration(60)
        talk2.set_name("B")

        shift.add_talk(talk1)
        shift.add_talk(talk2)

        self.assertEquals("A", shift.talks[0].get_name())
        self.assertEquals("B", shift.talks[1].get_name())

        self.assertEquals(65, shift.talks[0].get_duration())
        self.assertEquals(60, shift.talks[1].get_duration())


if __name__ == '__main__':
    unittest.main()
