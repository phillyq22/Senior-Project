from MapBuilder import SimMap
from datetime import datetime
from dateutil import rrule

simMap = SimMap()
simMap.takeUsers()

startDay = datetime(2018, 1, 1)
endYear = datetime(2018, 1, 2)

for dt in rrule.rrule(rrule.MINUTELY, dtstart=startDay, until=endYear):
    dateString = str(dt)[:-3]
    print(dt)
    if dateString in simMap.usersStart:
        print(simMap.usersStart[dateString])





