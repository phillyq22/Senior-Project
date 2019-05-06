from pandas import *
from dateutil import rrule
from datetime import datetime, timedelta
from progressbar import ProgressBar

# Looks at csv file and creates another csv file with the data cleaned up.

pbar = ProgressBar()

# Creates dataframe from our csv.
df = read_csv('unparsedData/2010-capitalbikeshare-tripdata.csv')
dic = { 'StartDate': [], 'EndDate': [], 'StartStation': []}
print('Size of input', len(df))

# Converts a date time to minute of the day.
def converter(x: datetime):
    result = x.hour * 60 + x.minute
    return result

# Loops through data frame and add important data to a dictionary.
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

# Loops though the stations and adds data for stations that did not have a bike taken at a given minute.
for stationNum in pbar(stationSet):
    for dt in rrule.rrule(rrule.HOURLY, dtstart=startDay, until=endYear):
        dic.get('StartDate').append(str(dt)[:-6])
        dic.get('EndDate').append(str(dt))
        dic.get('StartStation').append(stationNum)

# Creates new data frame an groups it by station id and start date.
newdf = DataFrame(data=dic)
grouped = newdf.groupby(['StartDate', 'StartStation'])
parsedDic = {'StartStation': [], 'DayOfWeek': [], 'Time': [], 'Month': [], 'Demand': []}
print('Size after parse', len(grouped))

# Sets up data to be exported.
for name, group in grouped:
    datetimeValue = datetime.strptime(name[0], '%Y-%m-%d %H')
    parsedDic.get('StartStation').append(name[1])
    parsedDic.get('DayOfWeek').append(datetimeValue.weekday())
    parsedDic.get('Time').append(converter(datetimeValue))
    parsedDic.get('Month').append(datetimeValue.month)
    parsedDic.get('Demand').append(len(group) - 1)





newdf = DataFrame(data=parsedDic)

newdf.to_csv('outSmall.csv')



