import pandas as pd
from progressbar import ProgressBar
from datetime import date
import sqlite3 as lite


'''
FYI: any reference to join_data, joinData, joined data or anything of that nature refers to the combination of the 
parsed station data and the weather data
'''




'''
Reads in the parsed data and weather data into respective variables
'''
parsed_data = pd.read_csv("./parsedData/Parsed2018_w0_wDates.csv")
weather_data = pd.read_csv("./WeatherData.csv")

'''
Creates Weather Dictionary for further use in database 
'''
weatherDic = {}
for i, row in enumerate(weather_data.values):
    id,maxSusWind,maxTemp,maxWind,meanDew,meanSeaPres,meanTemp,meanWind,minTemp,snowDepth,totPrecp,visibility = row
    weatherDic[id] = []
    weatherDic[id].append({'MaxSusWind': maxSusWind, "MaxTemp": maxTemp, "MaxWind": maxWind, "MeanDew": meanDew,
                        "MeanSeaPres": meanSeaPres, "MeanTemp": meanTemp, "MeanWind": meanWind, "MinTemp": minTemp,
                        "SnowDepth": snowDepth, "TotPrecp": totPrecp, "Visibility": visibility})

'''
Creates parsed data Dictionary for further use in database 
'''
parsedDic = {}
for i, row in enumerate(parsed_data.values):
    id, dayOfWeek, demand, month, startDate, startStation, time = row
    parsedDic[id] = []
    parsedDic[id].append({'dayOfWeek': dayOfWeek, 'Demand': demand, 'month': month, 'startDate': startDate,
                     'startStation': startStation, 'Time': time})


'''
Starts connection with database
'''
con = lite.connect('bikeWeatherData.db')
cur = con.cursor()


'''
Creates the table within the database for all the joined data
'''
def create_joinData():
    cur.execute("DROP TABLE IF EXISTS joinData")
    s = 'CREATE TABLE joinData(dayOfWeek Int2,demand Int2,month Int2,startDate VARCHAR(20),'
    s = s + 'startStation Int2,time VARCHAR(15), maxSusWind Float,maxTemp Float,maxWind Float,meanDew Float,meanSeaPres Float,'
    s = s + 'meanTemp Float,meanWind Float,minTemp Float, snowDepth Float,totalPrec float, visibility float, startDate2 VARCHAR(20))'
    print(s)
    cur.execute(s)

'''
Creates the table within the database for all the parsed data
'''
def create_data():
    cur.execute("DROP TABLE IF EXISTS data")
    s = 'CREATE TABLE data(dayOfWeek Int2,demand Int2,month Int2,startDate VARCHAR(20),'
    s = s + 'startStation Int2,time VARCHAR(15))'
    print(s)
    cur.execute(s)

'''
Creates the table within the database for all the weather data
'''
def create_weather():
    cur.execute("DROP TABLE IF EXISTS weather")
    s = 'CREATE TABLE weather(maxSusWind Float,maxTemp Float,maxWind Float,meanDew Float,meanSeaPres Float,'
    s = s + 'meanTemp Float,meanWind Float,minTemp Float, snowDepth Float,totalPrec float, visibility float, startDate VARCHAR(20))'
    print(s)
    cur.execute(s)
'''
Populates the parsed data table within the database
'''
def populate_parsedData(data):
    i = 0
    for row in data:
        i = i + 1
        try:
            cur.execute("INSERT INTO data VALUES (?,?,?,?,?,?)",
                        (row[0]['dayOfWeek'], row[0]['Demand'], row[0]['month'],
                         row[0]['startDate'][:-3], row[0]['startStation'], row[0]['Time']))
        except lite.OperationalError as err:
            print("insert error: %s", err)
        if i % 100 == 0:
            print("inserted row ", str(i))
            con.commit()
    return i

'''
Populates the weather data table within the database
'''
def populate_weatherData(data):
    i = 0
    for row in data:

        full_date = date.fromordinal(date(2018, 1, 1).toordinal() + i - 1)

        try:
            cur.execute("INSERT INTO weather VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                        (row[0]['MaxSusWind'], row[0]['MaxTemp'], row[0]['MaxWind'],
                         row[0]['MeanDew'], row[0]['MeanSeaPres'], row[0]['MeanTemp'], row[0]['MeanWind'], row[0]['MinTemp'],
                         row[0]['SnowDepth'], row[0]['TotPrecp'], row[0]['Visibility'], full_date))
        except lite.OperationalError as err:
            print("insert error: %s", err)
        if i % 100 == 0:
            print("inserted row ", str(i))
            con.commit()
        i = i + 1
    return i

'''
Populates the table with joined data between weather data and parsed data within the database
'''
def join_data():
    i = 0
    #cur.execute("SELECT count(*) FROM data")
    #numRows = cur.fetchall()
    #for i in range(0, numRows[0][0]):
    try:
        cur.execute("SELECT * FROM data INNER JOIN weather ON data.startDate = weather.startDate")
        rows = cur.fetchall()
        for row in rows:
            try:
                cur.execute("INSERT INTO joinData VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (row[0], row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8],
                             row[9], row[10], row[11], row[12], row[13],
                             row[14], row[15], row[16], row[17]))

            except lite.OperationalError as err:
                print("insert error: %s", err)
            if i % 100 == 0:
                print("inserted row ", str(i))
                con.commit()
            i = i + 1
    except lite.OperationalError as err:
        print("join error: %s", err)


'''
Uncomment each depending on which part of database you would like to build
'''
#create_data()
#create_weather()

#populate_weatherData(weatherDic.values())
#populate_parsedData(parsedDic.values())\

#create_joinData()
#join_data()

'''
Creates the dictionary for joined data
'''

joinDic = {'dayOfWeek': [], 'demand': [], 'month': [], 'startDate': [],
                     'startStation': [], 'time': [], 'maxSusWind': [], "maxTemp": [], "maxWind": [], "meanDew": [],
                        "meanSeaPres": [], "meanTemp": [], "meanWind": [], "minTemp": [],
                        "snowDepth": [], "totalPrec": [], "visibility": [], "startDate2": []}


#cur.execute("select * from joinData")
'''
Populates dictionary of joined data
'''
rows = cur.fetchall()
i = 0
for row in rows:
    dayOfWeek, demand, month, startDate, startStation, time, maxSusWind, maxTemp, maxWind, meanDew, meanSeaPres, meanTemp, meanWind, minTemp, snowDepth, totalPrec, visibility, startDate2 = row
    joinDic['dayOfWeek'].append(dayOfWeek)
    joinDic['demand'].append(demand)
    joinDic['month'].append(month)
    joinDic['startDate'].append(startDate)
    joinDic['time'].append(time)
    joinDic['maxSusWind'].append(maxSusWind)
    joinDic['maxTemp'].append(maxTemp)
    joinDic['maxWind'].append(maxWind)
    joinDic['meanDew'].append(meanDew)
    joinDic['meanSeaPres'].append(meanSeaPres)
    joinDic['meanTemp'].append(meanTemp)
    joinDic['meanWind'].append(meanWind)
    joinDic['minTemp'].append(minTemp)
    joinDic['snowDepth'].append(snowDepth)
    joinDic['totalPrec'].append(totalPrec)
    joinDic['visibility'].append(visibility)
    joinDic['startDate2'].append(startDate2)
    i = i + 1
    print("inserted")
    print(i)

'''
exports joined data into csv
'''
df = pd.DataFrame(data=joinDic)
df.to_csv('./finalWeatherData.csv')


#cur.execute("SELECT count(*) FROM data")
#numRows = cur.fetchall()
#print(numRows[0][0])
