from MapBuilder import SimMap
from EndLocation import *
from BikeAlg import *
from Station import Station
from User import User
import Scorer
from datetime import datetime
from dateutil import rrule

STATIONRADIUS = 1
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
simMap.calculateStationBaseline()
STATIONLIST = list(simMap.stations.values())


startDay = datetime(2018, 6, 7)
endYear = datetime(2018, 6, 8)


for dt in rrule.rrule(rrule.MINUTELY, dtstart=startDay, until=endYear):
    dateString = str(dt)[:-3]
    print(dt)
    print('Start Times: ')
    if dateString in simMap.usersStart:
        for user in simMap.usersStart[dateString]:
            print(user)
            print('START STATION:  ', user.startStation)

            ba = BikeAlg()
            loc = EndLocation(user.startLocation[0], user.startLocation[1])
            ba.preProcess(STATIONLIST, loc)
            ba.getWithin(loc, STATIONRADIUS)

            for startStation in loc.sortedAdj: #LIST STATION CLOSE BY
                startStationId = startStation.station.id
                if simMap.stations[startStationId].isBikeAvail():
                    user.startStation = startStationId
                    break

            if user.startStation in simMap.stations:
                if simMap.stations[user.startStation].isBikeAvail():
                    simMap.stations[user.startStation].decreaseBikeAvail()
                    nonErrors += 1
                else:
                    stationsBikeUnavail.append(user.startStation)
                    BikeUnavailErrors += 1
            else:
                missingStations.append(user.startStation)
                stationMissingErrors += 1


            if user.endDateTime in simMap.usersEnding:
                simMap.usersEnding[user.endDateTime].append(user)
            else:
                simMap.usersEnding[user.endDateTime] = []
                simMap.usersEnding[user.endDateTime].append(user)

    print('End Times: ')
    if dateString in simMap.usersEnding:
        for user in simMap.usersEnding[dateString]:
            print(user)

            # UPDATE USER END STATION BASED ON END LOCATION
            ba = BikeAlg()
            loc = EndLocation(user.endLocation[0], user.endLocation[1])
            ba.preProcess(STATIONLIST, loc)
            ba.getSuggest(loc, STATIONRADIUS, 0)


            # THIS IS WHERE WE TELL THE USER TO GO.
            for endStation in loc.sortedSug: #LIST STATION CLOSE BY
                endStationId = endStation.station.id
                if simMap.stations[endStationId].isDocAvail():
                    user.endStation = endStationId
                    break

            if user.endStation in simMap.stations:
                if simMap.stations[user.endStation].isDocAvail():
                    simMap.stations[user.endStation].increaseBikeAvail()
                    nonErrors += 1
                else:
                    stationsDocUnavail.append(user.endStation)
                    DocUnavailErrors += 1
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
print('prp: ', Station.prop)
with open('StationJson/StationDataOut.json', 'w') as outfile:
    simMap.generateStationJson(outfile)

#print(list(simMap.stations.keys()))

Scorer.scorer('StationJson/StationDataOut.json')

