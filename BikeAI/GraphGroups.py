from pandas import *
import time
from NormalPredict import *
from datetime import datetime
from dateutil import rrule
import os

#NEED A WAY TO DIFFER DATES!!!!


parsedDic = {'StartStation': [], 'DayOfWeek': [], 'Time': [], 'Month': [], 'Demand': []}
df = read_csv("parsedData/Parsed2018_withzero.csv")

grouped = df.groupby(['StartStation', 'DayOfWeek', 'Month'])

for name, group in grouped:
    #print(name)
    print(group)
    demandArray = []
    for i, row in enumerate(group.values):
        demandArray.append([row[5], row[2]])
        if row[2] == 0:
            continue
        if row[5] == 1380:
            break

    print(demandArray)
    normModel = NormalModel()
    normModel.fitModel(demandArray, True)

