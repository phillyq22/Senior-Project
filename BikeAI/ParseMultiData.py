from pandas import *
from datetime import datetime
from dateutil import rrule
import os


dic = { 'StartDate': [], 'EndDate': [], 'StartStation': []}

#listOfData = ['201801_capitalbikeshare_tripdata.csv', '201802-capitalbikeshare-tripdata.csv', '201803-capitalbikeshare-tripdata.csv', '201804-capitalbikeshare-tripdata.csv', '201805-capitalbikeshare-tripdata.csv', '201806-capitalbikeshare-tripdata.csv', '201807-capitalbikeshare-tripdata.csv', '201808-capitalbikeshare-tripdata.csv', '201809-capitalbikeshare-tripdata.csv', '201810-capitalbikeshare-tripdata.csv', '201811-capitalbikeshare-tripdata.csv', '201812-capitalbikeshare-tripdata.csv']


def converter(x: datetime):
    result = x.hour * 60 + x.minute
    return result


for dataString in os.listdir('unparsedData'):
    if dataString.endswith(".csv"):
        df = read_csv("unparsedData/" + dataString)
        print('File: ', dataString, ' Size of input', len(df))

        for i, row in enumerate(df.values):
            date = df.index[i]
            duration, startDate, endDate, startStationNumber, startStationLoc, endSationNumber, endStationLoc, bikeNumber, memberType = row
            dic.get('StartDate').append(startDate[:-6])
            dic.get('EndDate').append(endDate)
            dic.get('StartStation').append(startStationNumber)


stationSet = set(dic.get('StartStation'))

startDay = datetime(2010, 9, 1)
endYear = datetime(2019, 1, 1)

for stationNum in stationSet:
    for dt in rrule.rrule(rrule.HOURLY, dtstart=startDay, until=endYear):
        dic.get('StartDate').append(str(dt)[:-6])
        dic.get('EndDate').append(str(dt))
        dic.get('StartStation').append(stationNum)

newdf = DataFrame(data=dic)
print('Size of input: ', len(newdf))
grouped = newdf.groupby(['StartDate', 'StartStation'])
parsedDic = {'StartStation': [], 'DayOfWeek': [], 'Time:': [], 'Month': [], 'Demand': []}
print('Size after parse', len(grouped))

for name, group in grouped:
    datetimeValue = datetime.strptime(name[0], '%Y-%m-%d %H')
    parsedDic.get('StartStation').append(name[1])
    parsedDic.get('DayOfWeek').append(datetimeValue.weekday())
    parsedDic.get('Time').append(converter(datetimeValue))
    parsedDic.get('Month').append(datetimeValue.month)
    parsedDic.get('Demand').append(len(group) - 1)

newdf = DataFrame(data=parsedDic)

newdf.to_csv('out.csv')



