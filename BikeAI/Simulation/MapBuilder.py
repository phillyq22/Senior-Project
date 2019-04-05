import json
from pandas import *
from datetime import datetime
from dateutil import rrule
import os
import gc

class SimMap:

    def __init__(self):
        self.stations = {}
        self.users = {}

    def takeUsers(self):
        for dataString in os.listdir('UserData'):
            if dataString.endswith(".csv"):
                df = read_csv("UserData/" + dataString)
                print('File: ', dataString, ' Size of input', len(df))

                for i, row in enumerate(df.values):
                    userDic = {'StartDate': [], 'EndDate': [], 'StartStation': [], 'EndStation': []}
                    date = df.index[i]
                    duration, startDate, endDate, startStationNumber, startStationLoc, endSationNumber, endStationLoc, bikeNumber, memberType = row
                    userDic.get('StartDate').append(str(startDate)[:-6])
                    userDic.get('EndDate').append(str(endDate)[:-6])
                    userDic.get('StartStation').append(startStationNumber)
                    userDic.get('EndStation').append(endSationNumber)
                    if str(startDate)[:-6] in self.users:
                        self.users[str(startDate)[:-6]].append(userDic)
                    else:
                        self.users[str(startDate)[:-6]] = []
                        self.users[str(startDate)[:-6]].append(userDic)
        print(self.users)


simMap = SimMap()
simMap.takeUsers()




