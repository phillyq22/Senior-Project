import json as jsonCreator
from pandas import *
from Station import Station
from User import User
from datetime import datetime
from dateutil import rrule
import os
import gc
import random

END_LOCATION_RADIUS = 1

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
                    userDic.get('StartDate').append(str(startDate)[:-3])
                    userDic.get('EndDate').append(str(endDate)[:-3])
                    userDic.get('StartStation').append(startStationNumber)
                    userDic.get('EndStation').append(endSationNumber)

                    newUser = User(startStationNumber, endSationNumber, self.generateRandomLocaton(endSationNumber),
                                   str(endDate)[:-3])

                    if str(startDate)[:-3] in self.usersStart:
                        self.usersStart[str(startDate)[:-3]].append(newUser)
                    else:
                        self.usersStart[str(startDate)[:-3]] = []
                        self.usersStart[str(startDate)[:-3]].append(newUser)
        #print(list(self.users.keys())[0])
        #print(self.users[list(self.users.keys())[0]])


    def generateRandomLocaton(self, stationId):
        #longitude = self.stations[stationId].longitude + random.randint(0, END_LOCATION_RADIUS)
        #latitude = self.stations[stationId].latitude + random.randint(0, END_LOCATION_RADIUS)
        #return [longitude, latitude]
        return [random.randint(0, 100), random.randint(0, 100)]


    def generateStationJson(self, outFile):
        return jsonCreator.dump(list(self.stations.values()), outFile, default=lambda o: o.toJSON(), sort_keys=True, indent=4)


'''
s1 = Station(jsonText='{"id": "1", "name": "lal", "longiude": 3, "latitude": 6, "nec": "NAN", "bikeAvail": 4, "docAvail": 7}')
sm = SimMap()
sm.stations['1'] = s1
s1 = Station(jsonText='{"id": "1", "name": "lal", "longiude": 3, "latitude": 6, "nec": "NAN", "bikeAvail": 4, "docAvail": 7}')
sm.stations['2'] = s1
s1 = Station(jsonText='{"id": "1", "name": "lal", "longiude": 3, "latitude": 6, "nec": "NAN", "bikeAvail": 4, "docAvail": 7}')
sm.stations['3'] = s1


with open('StationJson/data.json', 'w') as outfile:
    sm.generateStationJson(outfile)
'''
