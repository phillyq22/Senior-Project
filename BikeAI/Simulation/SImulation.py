from MapBuilder import SimMap
from Station import Station
from User import User
from datetime import datetime
from dateutil import rrule

simMap = SimMap()
simMap.takeUsers()

startDay = datetime(2018, 1, 1)
endYear = datetime(2018, 1, 2)

for dt in rrule.rrule(rrule.MINUTELY, dtstart=startDay, until=endYear):
    dateString = str(dt)[:-3]
    print(dt)
    print('Start Times: ')
    if dateString in simMap.usersStart:
        for user in simMap.usersStart[dateString]:
            print(user)

            if user.startStation in simMap.stations:
                simMap.stations[user.startStation].decreaseBikeAvail()

            #UPDATE USER END STATION BASED ON END LOCATION
            if user.endDateTime in simMap.usersEnding:
                simMap.usersEnding[user.endDateTime].append(user)
            else:
                simMap.usersEnding[user.endDateTime] = []
                simMap.usersEnding[user.endDateTime].append(user)

    print('End Times: ')
    if dateString in simMap.usersEnding:
        for user in simMap.usersEnding[dateString]:
            print(user)

            if user.endStation in simMap.stations:
                simMap.stations[user.endStation].increaseBikeAvail()

