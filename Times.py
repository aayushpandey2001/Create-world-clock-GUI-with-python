#this lines of code is only for check the all countries time zones, so Guys don't massup this in our program

import pytz


for tz in pytz.all_timezones:
    print(tz)
