import unittest

from src.service.io.talk_reader import TalkReader


class TalkReaderTestCase(unittest.TestCase):

    def setUp(self):
        self.talk_reader = TalkReader()

    @unittest.expectedFailure
    def test_parse_line_failure_with_empty(self):
        self.talk_reader._parse_line(" ")

    @unittest.expectedFailure
    def test_parse_line_failure_with_new_line(self):
        self.talk_reader._parse_line("\n")

    @unittest.expectedFailure
    def test_parse_duration_failure_without_time(self):
        self.talk_reader._parse_duration("Pair Programming vs Noise")

    @unittest.expectedFailure
    def test_parse_duration_failure_without_lightning(self):
        self.talk_reader._parse_duration("Lightninged and Lightnings")

    def test_parse_duration(self):
        self.assertEquals(
            self.talk_reader._parse_duration("Pair Programming vs Noise 45min"),
            45
        )
        self.assertEquals(
            self.talk_reader._parse_duration("Ruby on Rails: Why We Should Move On 60min"),
            60
        )
        self.assertEquals(
            self.talk_reader._parse_duration("Rails for Python Developers lightning"),
            5
        )

    def test_parse_name(self):
        self.assertEquals(
            self.talk_reader._parse_name("Pair Programming vs Noise 45min"),
            "Pair Programming vs Noise"
        )
        self.assertEquals(
            self.talk_reader._parse_name("Ruby on Rails: Why We Should Move On 60min"),
            "Ruby on Rails: Why We Should Move On"
        )
        self.assertEquals(
            self.talk_reader._parse_name("Rails for Python Developers lightning"),
            "Rails for Python Developers"
        )

    def test_parse(self):
        first_talk = self.talk_reader._parse("Pair Programming vs Noise 45min")
        self.assertEquals(45, first_talk.get_duration())
        self.assertEquals("Pair Programming vs Noise", first_talk.get_name())

        second_talk = self.talk_reader._parse("Rails for Python Developers lightning")
        self.assertEquals(5, second_talk.get_duration())
        self.assertEquals("Rails for Python Developers", second_talk.get_name())


if __name__ == '__main__':
    unittest.main()
