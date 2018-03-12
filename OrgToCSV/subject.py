# subject.py
#
# Represent a Subject in an .org file
#
# Subject Class:
#               - name                               : STRING
#               - total duration studied             : number
#               - total times studied in general     : number
#               - total times studied by day of week : number list
#
# Example:
#         ** CSCI 2041 [2/4]
#            :LOGBOOK:
#            CLOCK: [yyyy-mm-dd Dow hh:mm]--[yyyy-mm-dd Dow hh:mm] =>  1:15
#            :END:
#
###############################################################################


class Subject:

    def __init__(self, name):
        self.name = name
        self.duration = 0
        self.times_studied = 0
        self.duration_by_day = [0, 0, 0, 0, 0, 0, 0]
        self.times_studied_by_day = [0, 0, 0, 0, 0, 0, 0]

    def get_name(self):
        return self.name

    def get_duration(self):
        return self.duration

    def get_times_studied(self):
        return self.times_studied

    def get_duration_by_day(self):
        return self.duration_by_day

    def get_times_studied_by_day(self):
        return self.times_studied_by_day

    def increment_duration(self, dur):
        self.duration = self.duration + dur

    def increment_times_studied(self):
        self.times_studied = self.times_studied + 1

    def get_day_index(self, day):
        day_dictionary = {
            'Mon': 0,
            'Tue': 1,
            'Wed': 2,
            'Thu': 3,
            'Fri': 4,
            'Sat': 5,
            'Sun': 6,
        }

        if day in day_dictionary:
            return day_dictionary[day]
        else:
            print("Error in subject.py get_day_index:")
            print("\t" + day + " was not found in day_dictionary.")
            return -1

    def increment_duration_day(self, dur, day):
        day_index = self.get_day_index(day)
        # TODO : error checking on day_index being -1
        if day_index >= 0:
            self.duration_by_day[day_index] += dur
            print("Incremented duration by day")
        else:
            print("Did not increment duration by day")

    def increment_times_studied_day(self, day):
        day_index = self.get_day_index(day)
        # TODO : error checking on day_index being -1
        if day_index >= 0:
            self.times_studied_by_day[day_index] += 1
            print("Incremented times studied by day")
        else:
            print("Did not increment times studied by day")
