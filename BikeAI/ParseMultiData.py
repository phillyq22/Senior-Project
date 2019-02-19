from pandas import *
from datetime import datetime
from progressbar import ProgressBar

pbar = ProgressBar()


dic = { 'StartDate': [], 'EndDate': [], 'StartStation': []}

listOfData = ['201801_capitalbikeshare_tripdata.csv', '201802-capitalbikeshare-tripdata.csv', '201803-capitalbikeshare-tripdata.csv', '201804-capitalbikeshare-tripdata.csv', '201805-capitalbikeshare-tripdata.csv', '201806-capitalbikeshare-tripdata.csv', '201807-capitalbikeshare-tripdata.csv', '201808-capitalbikeshare-tripdata.csv', '201809-capitalbikeshare-tripdata.csv', '201810-capitalbikeshare-tripdata.csv', '201811-capitalbikeshare-tripdata.csv', '201812-capitalbikeshare-tripdata.csv']

for dataString in listOfData:
    df = read_csv(dataString)
    print('File: ', dataString, ' Size of input', len(df))


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
print('Size after parse', len(grouped))

for name, group in pbar(grouped):
    datetimeValue = datetime.strptime(name[0], '%Y-%m-%d %H:%M')
    parsedDic.get('StartStation').append(name[1])
    parsedDic.get('DayOfWeek').append(datetimeValue.weekday())
    parsedDic.get('Time').append(converter(datetimeValue))
    parsedDic.get('Month').append(datetimeValue.month)
    parsedDic.get('Demand').append(len(group))

newdf = DataFrame(data=parsedDic)

newdf.to_csv('out.csv')



