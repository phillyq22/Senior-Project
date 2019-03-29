from pandas import *
from NormalPredict import *

THRESHOLD = 3

parsedDic = {'StartStation': [], 'DayOfWeek': [], 'Time': [], 'Month': [], 'Demand': []}
df = read_csv("parsedData/Parsed2018_withzero.csv")

grouped = df.groupby(['StartStation', 'DayOfWeek', 'Month'])

for name, group in grouped:
    #print(name)
    print(group)
    demandArray = []
    for i, row in enumerate(group.values):
        demandArray.append([row[5], row[2]])


    print(demandArray)
    normModel = NormalModel()
    normModel.fitModel(demandArray, True)

