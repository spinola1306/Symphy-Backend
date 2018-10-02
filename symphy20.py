#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

import platform


print(platform.python_version())

from croniter import croniter
from datetime import datetime
base = datetime(2010, 1, 25, 4, 46)
iter = croniter('*/5 * * * *', base)  # every 5 minutes
print(iter.get_next(datetime))   # 2010-01-25 04:50:00




chedule = "*/5 * * * *" # Run every five minutes

nextRunTime = getNextCronRunTime(schedule)
while True:
     roundedDownTime = roundDownTime()
     if (roundedDownTime == nextRunTime):
         ####################################
         ### Do your periodic thing here. ###
         ####################################
         nextRunTime = getNextCronRunTime(schedule)
     elif (roundedDownTime > nextRunTime):
         # We missed an execution. Error. Re initialize.
         nextRunTime = getNextCronRunTime(schedule)
     sleepTillTopOfNextMinute()



	 
	 from croniter import croniter
from datetime import datetime, timedelta

# Round time down to the top of the previous minute
def roundDownTime(dt=None, dateDelta=timedelta(minutes=1)):
    roundTo = dateDelta.total_seconds()
    if dt == None : dt = datetime.now()
    seconds = (dt - dt.min).seconds
    rounding = (seconds+roundTo/2) // roundTo * roundTo
    return dt + timedelta(0,rounding-seconds,-dt.microsecond)

# Get next run time from now, based on schedule specified by cron string
def getNextCronRunTime(schedule):
    return croniter(schedule, datetime.now()).get_next(datetime)

# Sleep till the top of the next minute
def sleepTillTopOfNextMinute():
    t = datetime.utcnow()
    sleeptime = 60 - (t.second + t.microsecond/1000000.0)
    time.sleep(sleeptime)