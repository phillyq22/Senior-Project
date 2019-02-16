from pandas import *
from datetime import datetime


df = read_csv('bikeShareData.csv')
dic = { 'StartDate': [], 'EndDate': [], 'StartStation': []}


def converter(x: datetime):
    result = x.hour * 60 + x.minute
    return result


for i, row in enumerate(df.values):
    date = df.index[i]
    duration, startDate, endDate, startStationNumber, startStationLoc, endSationNumber, endStationLoc, bikeNumber, memberType = row
    dic.get('StartDate').append(startDate[:-3])
    dic.get('EndDate').append(endDate)
    dic.get('StartStation').append(startStationNumber)


newdf = DataFrame(data=dic)
grouped = newdf.groupby(['StartDate', 'StartStation'])
parsedDic = {'StartStation': [], 'DayOfWeek': [], 'Time': [], 'Month': [], 'Demand': []}

for name, group in grouped:
    datetimeValue = datetime.strptime(name[0], '%Y-%m-%d %H:%M')
    parsedDic.get('StartStation').append(name[1])
    parsedDic.get('DayOfWeek').append(datetimeValue.weekday())
    parsedDic.get('Time').append(converter(datetimeValue))
    parsedDic.get('Month').append(datetimeValue.month)
    parsedDic.get('Demand').append(len(group))
    newdf = DataFrame(data=parsedDic)

newdf.to_csv('out.csv')



