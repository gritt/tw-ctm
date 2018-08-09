from src.service.io.stdin_talks_parser import StdinTalksParser

__author__ = 'gritt'


class App:

    def __init__(self):
        self.stdin_talks_parser = StdinTalksParser()

    def execute(self):
        try:

            talks = self.stdin_talks_parser.process()


        except Exception as ex:
            print(ex.message)
        except EnvironmentError as ex:
            print(ex.message)


App = App()
App.execute()
