from pandas import *
import pickle

reg = pickle.load( open( "file", "rb"))


def testSingleStation(dayOfWeek, month, startStation, time, maxSusWind, maxTemp, maxWind, meandDew, meanTemp, meanWind, minTemp, snowDepth, totalPrec, visibility) :
    dic = {'DayOfWeek': [dayOfWeek], 'Month': [month], 'StartStation': [startStation], 'Time': [time],
           'Max sus Wind': [maxSusWind], 'Max Temp': [maxTemp], 'MaxWind': [maxWind], 'meanDew': [meandDew], 'meanTemp': [meanTemp],
           'meanWind': [meanWind], 'minTemp': [minTemp], 'snowDepth': [snowDepth], 'totalPrec': [totalPrec], 'visibility': [visibility]}
    newdf = DataFrame(data=dic)
    return reg.predict(newdf).round()