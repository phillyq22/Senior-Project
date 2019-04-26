from pandas import *
import pickle

reg = pickle.load(open("file", "rb"))

maxSusWind = 17.26
maxTemp = 25.9
maxWind = 0.0
meanDew = 0.0
meanTemp = 17.9
meanWind = 8.17
minTemp = 13.3
snowDepth = 0.0
totalPrec = 0.0
visibility = 0.0

defaultMonth = 6
defaultDayOfWeek = 5


def testSingleStation(startStation, month, dayOfWeek, time) :


#for Loop for making it per hour (12 am 1 am 2 am etc etc)


    dic = {'DayOfWeek': [dayOfWeek], 'Month': [month], 'StartStation': [startStation], 'Time': [time],
           'Max sus Wind': [maxSusWind], 'Max Temp': [maxTemp], 'MaxWind': [maxWind], 'meanDew': [meanDew],
           'meanTemp': [meanTemp],'meanWind': [meanWind], 'minTemp': [minTemp], 'snowDepth': [snowDepth],
           'totalPrec': [totalPrec], 'visibility': [visibility]}
    newdf = DataFrame(data=dic)
    return round(reg.predict(newdf)[0])
    #return reg.score().round()[0]


def twentyFourHourTest(startStation, month = defaultMonth, dayOfWeek = defaultDayOfWeek):
    arrayOfDemand = []
    i = 0000
    x = 0
    for x in range(24):
        arrayOfDemand.append(testSingleStation(startStation=startStation, month=month, dayOfWeek=dayOfWeek, time=i))
        x = x + 1
        i = i + 100
    return arrayOfDemand
'''
for i in range(24):
    print(i)
    i = i + 1
'''
print(twentyFourHourTest(31068)) #31021

#print(testSingleStation(startStation=31021, month=3, dayOfWeek=2, time=120))