from pandas import *
import pickle

reg = pickle.load(open("file", "rb"))

maxSusWind = 12.3
maxTemp = 80.0
maxWind = 17.0
meanDew = 0.0
meanTemp = 75.0
meanWind = 14.5
minTemp = 65.0
snowDepth = 0.0
totalPrec = 0.0
visibility = 0.0




def testSingleStation(startStation, month, dayOfWeek, time) :


#for Loop for making it per hour (12 am 1 am 2 am etc etc)


    dic = {'DayOfWeek': [dayOfWeek], 'Month': [month], 'StartStation': [startStation], 'Time': [time],
           'Max sus Wind': [maxSusWind], 'Max Temp': [maxTemp], 'MaxWind': [maxWind], 'meanDew': [meanDew],
           'meanTemp': [meanTemp],'meanWind': [meanWind], 'minTemp': [minTemp], 'snowDepth': [snowDepth],
           'totalPrec': [totalPrec], 'visibility': [visibility]}
    newdf = DataFrame(data=dic)
    return reg.predict(newdf).round()[0]

def twentyFourHourTest(startStation, month, dayOfWeek):
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
print(twentyFourHourTest(31021, 12, 25))

#print(testSingleStation(startStation=31021, month=3, dayOfWeek=2, time=120))