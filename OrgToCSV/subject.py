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

class Subject:

    def __init__(self, name):
        self.name = name
        self.duration = 0
        self.times_studied = 0
        self.duration_by_day = [0, 0, 0, 0, 0, 0, 0]
        self.time_studied_by_day = [0, 0, 0, 0, 0, 0, 0]


c1 = Subject("CSCI 2041")
c1.duration = 4

print(c1.name)
print(c1.duration)
