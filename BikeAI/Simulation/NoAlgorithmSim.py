from MapBuilder import SimMap
from Station import Station
from User import User
from Scorer import Scorer
from datetime import datetime
from dateutil import rrule

missingStations = []
stationsDocUnavail = []
stationsBikeUnavail = []
stationMissingErrors = 0
DocUnavailErrors = 0
BikeUnavailErrors = 0
nonErrors = 0
simMap = SimMap()
simMap.takeStations()
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
            print('START STATION:  ', user.startStation)
            if user.startStation in simMap.stations:
                if simMap.stations[user.startStation].isBikeAvail():
                    simMap.stations[user.startStation].decreaseBikeAvail()
                    nonErrors += 1
                else:
                    stationsBikeUnavail.append(user.startStation)
                    BikeUnavailErrors+=1
            else:
                missingStations.append(user.startStation)
                stationMissingErrors += 1

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
                if simMap.stations[user.endStation].isDocAvail():
                    simMap.stations[user.endStation].increaseBikeAvail()
                    nonErrors += 1
                else:
                    stationsDocUnavail.append(user.endStation)
                    DocUnavailErrors+=1
            else:
                missingStations.append(user.endStation)
                stationMissingErrors += 1


print('Station Missing: ', stationMissingErrors)
print('Missing Stations: ', set(missingStations))
print('Doc Unavail Errors: ', DocUnavailErrors)
print('Doc  Unavail Stations: ', set(stationsDocUnavail))
print('Bike Unavail Errors: ', BikeUnavailErrors)
print('Bike  Unavail Stations: ', set(stationsBikeUnavail))
print('Nonerrors: ', nonErrors)

with open('StationJson/StationDataOut.json', 'w') as outfile:
    simMap.generateStationJson(outfile)

#print(list(simMap.stations.keys()))

Scorer().scorer('StationJson/StationDataOut.json')

