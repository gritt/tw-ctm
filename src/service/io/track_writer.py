import datetime

__author__ = 'gritt'


class TrackWriter:

    def __init__(self):
        pass

    def present(self, tracks):

        for track in tracks:

            # prints track day
            print 'Track ' + str(track.get_day()) + ':'

            # prints track shifts (morning, afternoon)
            for shift in track.get_shifts():

                # shifts have a star_time and an end_time
                # eg: morning starts at 9, ends at 12

                # start tracking time
                timer = datetime.timedelta(
                    hours=shift.get_start_time(),
                    minutes=00
                )

                # prints talks scheduled for this shift
                for talk in shift.talks:
                    self._print_talk(talk, timer)

                    # next talk starts at current time + ongoing talk duration
                    timer += datetime.timedelta(minutes=talk.get_duration())

                # prints shift ending (lunch, networking)
                self._print_shift_end(shift)

            print "\n"

    def _print_talk(self, talk, timer):

        duration = str(talk.get_duration()) + 'min'

        if talk.get_duration() == 5:
            duration = "lightning"

        # in order to format the timer (datetime.timedelta)
        friendly_time = (datetime.datetime(1900, 1, 1) + timer).strftime('%I:%M%p')

        print friendly_time + " " + talk.get_name() + " " + duration

    def _print_shift_end(self, shift):

        if shift.get_end_time() == 17:
            print "05:00PM Networking Event"

        if shift.get_end_time() == 12:
            print "12:00PM Lunch"
