from src.service.io.talk_reader import TalkReader
from src.service.scheduler.scheduler import Scheduler

__author__ = 'gritt'


class App:

    def __init__(self):
        self.talk_reader = TalkReader()
        self.scheduler = Scheduler()

    def execute(self):
        try:

            talks = self.talk_reader.read_from_stdin()

            tracks = self.scheduler.schedule(talks)

        except Exception as ex:
            print(ex.message)


App = App()
App.execute()
