from MapBuilder import SimMap
from EndLocation import *
from BikeAlg import *
from Station import Station
import Scorer
from datetime import datetime
from dateutil import rrule
import random


'''Setting up initial parameters for the simulation.'''
STATIONRADIUS = float(input('Station radius: '))
INCENTIVEPERCENT = int(input('Percentage incentive is taken: '))
missingStations = []
stationsDocUnavail = []
stationsBikeUnavail = []
stationMissingErrors = 0
DocUnavailErrors = 0
BikeUnavailErrors = 0
nonErrors = 0
simMap = SimMap()
simMap.takeStationsFromJson()
simMap.takeUsers()
simMap.calculateStationBaseline()
STATIONLIST = list(simMap.stations.values())


startDay = datetime(2018, 6, 7)
endYear = datetime(2018, 6, 8)


# Simulation loop will run from startDay to endYear.
for dt in rrule.rrule(rrule.MINUTELY, dtstart=startDay, until=endYear):
    dateString = str(dt)[:-3]# Current time the simulation is on.
    print(dt)
    print('Start Times: ')
    '''First if statement making a transaction whenever the dateString matches a transaction
     time in the user dictionary.'''
    if dateString in simMap.usersStart:
        for user in simMap.usersStart[dateString]:
            print(user)
            print('START STATION:  ', user.startStation)

            # Gets all stations within a radius and is sorted by distance.
            ba = BikeAlg(STATIONRADIUS)
            loc = EndLocation(user.startLocation[0], user.startLocation[1])
            ba.preProcess(STATIONLIST, loc)
            ba.getWithin(loc)

            # Loops the the sorted station list to find the closest station with an open bike
            for startStation in loc.sortedAdj: #LIST STATION CLOSE BY
                startStationId = startStation.station.id
                # If bike is available then stop searching.
                if simMap.stations[startStationId].isBikeAvail():
                    user.startStation = startStationId
                    break

            # If staion exists, take bike.
            if user.startStation in simMap.stations:
                # If there's a bike at the station take bike else increase error count.
                if simMap.stations[user.startStation].isBikeAvail():
                    simMap.stations[user.startStation].decreaseBikeAvail()
                    nonErrors += 1
                else:
                    stationsBikeUnavail.append(user.startStation)
                    BikeUnavailErrors += 1
            # If station doesn't exist increase error counter.
            else:
                missingStations.append(user.startStation)
                stationMissingErrors += 1

            # Add a user to end locations.
            if user.endDateTime in simMap.usersEnding:
                simMap.usersEnding[user.endDateTime].append(user)
            else:
                simMap.usersEnding[user.endDateTime] = []
                simMap.usersEnding[user.endDateTime].append(user)

    # Block of code for users putting bikes back.
    print('End Times: ')
    if dateString in simMap.usersEnding:
        for user in simMap.usersEnding[dateString]:
            print(user)

            # Looks for the best stations to take a bike based off necessity and distance within a given radius.
            time = int((int(str(dt)[15:-3]) + int(str(dt)[12:-6]) * 60)/24)
            ba = BikeAlg(STATIONRADIUS)
            loc = EndLocation(user.endLocation[0], user.endLocation[1])
            ba.preProcess(STATIONLIST, loc)
            ba.getSuggest(loc, 0)

            randNum = random.randint(0,101)
            listToView = []
            # Will take a bike from our algorithm based off INCENTIVEPERCENT or it will use the closest station.
            if randNum < INCENTIVEPERCENT:
                listToView = loc.sortedSug
            else:
                listToView = loc.sortedAdj



            # Does the same thing as taking a bike but it drops it off instead.
            for endStation in listToView: #LIST STATION CLOSE BY
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


# Shows the stats of algorithm.
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

