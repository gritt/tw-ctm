__author__ = 'gritt'

import sys
import re

from src.entity.talk import Talk


class StdinTalksParser:

    def __init__(self):
        self.talks_list = []

    def process(self):

        for line in sys.stdin:
            try:

                talk = self._parse(line)
                self.talks_list.append(talk)

            except Exception as ex:
                continue

        return self.talks_list

    def _parse(self, line):

        self._validate(line)

        duration = self._parse_duration(line)
        name = self._parse_name(line)

        talk = Talk()
        talk.set_name(name)
        talk.set_duration(duration)

        return talk

    def _validate(self, line):

        if line == "\n" or len(line.strip()) == 0:
            raise Exception("Error: invalid empty line given")

        return 1

    def _parse_duration(self, line):

        if "lightning" in line:
            return 5

        matches = re.findall("\d+", line)
        if len(matches) == 1:
            return int(matches[0])

        raise Exception("Error: duration could not be parsed")

    def _parse_name(self, line):

        name = re.sub('([0-9])\w+', '', line)
        name = re.sub('lightning', '', name)
        return name.strip()
