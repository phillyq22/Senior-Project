

import json as JsonCreator
from pandas import *
from Station import Station
from CapitalBikeAPI import CapitalBikeAPI
from User import User
from datetime import datetime
from dateutil import rrule
import os
import gc
import random
random.seed(78787)
#28
END_LOCATION_RADIUS_DIVIDE_BY_10 = 3


class SimMap:

    def __init__(self):
        self.stations = {}
        self.usersStart = {}
        self.usersEnding = {}

    def takeUsers(self):
        for dataString in os.listdir('UserData'):
            if dataString.endswith(".csv"):
                df = read_csv("UserData/" + dataString)
                print('File: ', dataString, ' Size of input', len(df))

                for i, row in enumerate(df.values):
                    userDic = {'StartDate': [], 'EndDate': [], 'StartStation': [], 'EndStation': []}
                    date = df.index[i]
                    duration, startDate, endDate, startStationNumber, startStationLoc, endSationNumber, endStationLoc, bikeNumber, memberType = row
                    startStationNumber = str(startStationNumber)
                    endSationNumber = str(endSationNumber)
                    startDate = str(startDate)
                    endDate = str(endDate)
                    endSationNumber = str(endSationNumber)
                    startStationNumber = str(startStationNumber)
                    if startStationNumber in self.stations and endSationNumber in self.stations:
                        userDic.get('StartDate').append(startDate[:-3])
                        userDic.get('EndDate').append(endDate[:-3])
                        userDic.get('StartStation').append(startStationNumber)
                        userDic.get('EndStation').append(endSationNumber)

                        newUser = User(startStationNumber, endSationNumber, self.generateRandomLocaton(endSationNumber),
                                       endDate[:-3], [self.stations[startStationNumber].longitude, self.stations[startStationNumber].latitude])

                        if str(startDate)[:-3] in self.usersStart:
                            self.usersStart[startDate[:-3]].append(newUser)
                        else:
                            self.usersStart[startDate[:-3]] = []
                            self.usersStart[startDate[:-3]].append(newUser)
        #print(list(self.users.keys())[0])
        #print(self.users[list(self.users.keys())[0]])

    def takeStations(self):
        cb = CapitalBikeAPI()
        data = cb.create_simulation_json()
        data = data['stations']
        #print(data)
        for row in data:
            '''
            self.stations[row['id']] = Station(id=row['id'], longitude=row['longitude'],
                                                      latitude=row['latitude'], demand=row['demand'],
                                                      bikeAvail=row['bikeAvail'], docAvail=row['docAvail'],
                                                      capacity=row['capacity'])
            '''

            self.stations[row['id']] = Station(id=row['id'], longitude=row['longitude'],
                                                latitude=row['latitude'], demand=row['demand'],
                                                bikeAvail=16, docAvail=16,
                                                capacity=32)

    def takeStationsFromJson(self):
        path = 'data.json'
        with open(path) as json_file:
            data = JsonCreator.load(json_file)
            for field in data['stations']:
                self.stations[field['id']] = Station(id=field['id'], longitude=field['longitude'],
                                                   latitude=field['latitude'], demand=field['demand'],
                                                   bikeAvail=16, docAvail=16,
                                                   capacity=32)


    def generateRandomLocaton(self, stationId):
        if stationId in self.stations:
            while True:
                longitude = self.stations[str(stationId)].longitude + (random.randint(END_LOCATION_RADIUS_DIVIDE_BY_10 * -1, END_LOCATION_RADIUS_DIVIDE_BY_10)/69)
                if 90 > longitude > -90:
                    break

            while True:
                latitude = self.stations[str(stationId)].latitude + (random.randint(END_LOCATION_RADIUS_DIVIDE_BY_10 * -1, END_LOCATION_RADIUS_DIVIDE_BY_10)/69)
                if 90 > latitude > -90:
                    break

            return [longitude, latitude]
        else:
            return [random.randint(0, 100), random.randint(0, 100)]


    def generateStationJson(self, outFile):
        return JsonCreator.dump(list(self.stations.values()), outFile, default=lambda o: o.toJSON(), sort_keys=True, indent=4)

    def calculateStationBaseline(self):
        totalDocSize = 0
        totalBikes = 0
        for station in list(self.stations.values()):
            totalDocSize += station.capacity
            totalBikes += station.bikeAvail

        Station.prop = (totalBikes/totalDocSize)


'''
s1 = Station(jsonText='{"id": "1", "name": "lal", "longitude": 3, "latitude": 6, "nec": "NAN", "bikeAvail": 4, "docAvail": 7}')
sm = SimMap()
sm.stations['1'] = s1
s1 = Station(jsonText='{"id": "1", "name": "lal", "longitude": 3, "latitude": 6, "nec": "NAN", "bikeAvail": 4, "docAvail": 7}')
sm.stations['2'] = s1
s1 = Station(jsonText='{"id": "1", "name": "lal", "longitude": 3, "latitude": 6, "nec": "NAN", "bikeAvail": 4, "docAvail": 7}')
sm.stations['3'] = s1


with open('StationJson/data.json', 'w') as outfile:
    sm.generateStationJson(outfile)
'''
