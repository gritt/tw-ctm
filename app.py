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

            # TODO @gritt, display and handle clocking logic, implemente more tests and documentation

            for track in tracks:

                print '----Track' + "---" + str(track.get_day())

                for shift in track.get_shifts():

                    print "SHIFT HAS ---" + str(shift.get_minutes()) + "---" + str(shift.get_remaining_minutes())

                    for talk in shift.talks:
                        print talk.get_name() + "---" + str(talk.get_duration())



        except Exception as ex:
            print(ex.message)


App = App()
App.execute()
