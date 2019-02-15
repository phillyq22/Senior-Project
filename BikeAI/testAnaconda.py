from pandas import *
from datetime import datetime

df = read_csv('bikeShareData.csv')
dic = { 'StartDate' : [], 'EndDate' : []}


def converter(x: datetime):
    result = x.hour * 60 + x.minute
    return result


for i, row in enumerate(df.values):
    date = df.index[i]
    duration, startDate, endDate, startStationNumber, startStationLoc, endSationNumber, endStationLoc, bikeNumber, memberType = row
    dic.get('StartDate').append(startDate[:-3])
    dic.get('EndDate').append(endDate)

newdf = DataFrame(data=dic)
grouped = newdf.groupby('StartDate')
parsedDic = { 'DayOfWeek': [], 'Time': [], 'Month': [], 'Demand': []}
for name, group in grouped:
    datetimeValue = datetime.strptime(name, '%Y-%m-%d %H:%M')
    parsedDic.get('DayOfWeek').append(datetimeValue.weekday())
    parsedDic.get('Time').append(converter(datetimeValue))
    parsedDic.get('Month').append(datetimeValue.month)
    parsedDic.get('Demand').append(len(group))
    newdf = DataFrame(data=parsedDic)
newdf.to_csv('out.csv')



