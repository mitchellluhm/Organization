###############################################################################
# date.py
#
# Represent a Date in an .org file
#
# Date Class:
#            - date (yyyy-mm-dd)                : string
#            - day (Mon, Tues, etc)             : string
#            - duration studied on that date    : number
#            - number of study events that date : number
#
###############################################################################


class Date:

    def get_full_date_by_string(self, clock_str):
        return clock_str[11:21]

    def get_year_by_string(self, clock_str):
        return int(clock_str[11:15])

    def get_month_by_string(self, clock_str):
        return int(clock_str[16:18])

    def get_day_of_month_by_string(self, clock_str):
        return int(clock_str[19:21])

    def get_day_of_week_by_string(self, clock_str):
        return clock_str[22:25]

    def get_duration_studied_by_string(self, clock_str):
        dur_start = str.find(clock_str, "=> ") + 4
        dur_str = clock_str[dur_start:dur_start + 4]  # H:MM
        hour = int(dur_str[0])
        mins = int(dur_str[2:])
        return (hour * 60) + mins

    def increment_duration_by(self, dur):
        self.duration_studied += dur

    def __init__(self, clock_str):
        # clock_str:
        # CLOCK: [yyyy-mm-dd Dow hh:mm]--[yyyy-mm-dd Dow hh:mm] =>  1:15
        self.full_date = self.get_full_date_by_string(clock_str)
        self.year = self.get_year_by_string(clock_str)
        self.month = self.get_month_by_string(clock_str)
        self.day_of_month = self.get_day_of_month_by_string(clock_str)
        self.day_of_week = self.get_day_of_week_by_string(clock_str)
        self.duration_studied = self.get_duration_studied_by_string(clock_str)


d = Date("   CLOCK: [2018-03-01 Thu 10:00]--[2018-03-01 Thu 10:56] =>  0:56")
print(d.full_date)
print(d.year)
print(d.month)
print(d.day_of_month)
print(d.day_of_week)
print(d.duration_studied)
