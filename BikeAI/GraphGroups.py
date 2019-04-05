from pandas import *
import time
from NormalPredict import *
from datetime import datetime
from dateutil import rrule
import os



parsedDic = {'StartStation': [], 'DayOfWeek': [], 'Time': [], 'Month': [], 'Demand': []}
df = read_csv("Parsed2018WithDates.csv")

df.StartDate = df['StartDate'].str[:-2].astype(str)
grouped = df.groupby(['StartStation', 'StartDate'])

for name, group in grouped:
    if name[0] == 31012:
        #print(name)
        print(group)
        demandArray = []
        for i, row in enumerate(group.values):
            demandArray.append([row[6], row[2]])

        #print(demandArray)
        normModel = NormalModel()
        normModel.fitModel(demandArray, True)

