from pandas import *
from dateutil import rrule
from datetime import datetime, timedelta
from progressbar import ProgressBar

pbar = ProgressBar()

df = read_csv('unparsedData/2010-capitalbikeshare-tripdata.csv')
dic = { 'StartDate': [], 'EndDate': [], 'StartStation': []}
print('Size of input', len(df))


def converter(x: datetime):
    result = x.hour * 60 + x.minute
    return result


for i, row in enumerate(df.values):
    date = df.index[i]
    duration, startDate, endDate, startStationNumber, startStationLoc, endSationNumber, endStationLoc, bikeNumber, memberType = row
    dic.get('StartDate').append(startDate[:-6])
    dic.get('EndDate').append(endDate)
    dic.get('StartStation').append(startStationNumber)

stationSet = set(dic.get('StartStation'))

print(len(stationSet))

startDay = datetime(2010, 8, 1)
endYear = datetime(2011, 1, 31)

for stationNum in pbar(stationSet):
    for dt in rrule.rrule(rrule.HOURLY, dtstart=startDay, until=endYear):
        dic.get('StartDate').append(str(dt)[:-6])
        dic.get('EndDate').append(str(dt))
        dic.get('StartStation').append(stationNum)


newdf = DataFrame(data=dic)
grouped = newdf.groupby(['StartDate', 'StartStation'])
parsedDic = {'StartStation': [], 'DayOfWeek': [], 'Time': [], 'Month': [], 'Demand': []}
print('Size after parse', len(grouped))

for name, group in grouped:
    datetimeValue = datetime.strptime(name[0], '%Y-%m-%d %H')
    parsedDic.get('StartStation').append(name[1])
    parsedDic.get('DayOfWeek').append(datetimeValue.weekday())
    parsedDic.get('Time').append(converter(datetimeValue))
    parsedDic.get('Month').append(datetimeValue.month)
    parsedDic.get('Demand').append(len(group) - 1)





newdf = DataFrame(data=parsedDic)

newdf.to_csv('outSmall.csv')



