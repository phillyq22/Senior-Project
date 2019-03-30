import pandas as pd
from progressbar import ProgressBar
from datetime import date


import sqlite3 as lite



#pbar = ProgressBar()

parsed_data = pd.read_csv("./parsedData/Parsed2018_w0_wDates.csv")
weather_data = pd.read_csv("./WeatherData.csv")

#parsed_data = parsed_data.drop(columns="Unnamed: 0")
#weather_data = weather_data.drop(columns="Unnamed: 0")




#X = weather_data.iloc[[0]]

weatherDic = {}
for i, row in enumerate(weather_data.values):
    id,maxSusWind,maxTemp,maxWind,meanDew,meanSeaPres,meanTemp,meanWind,minTemp,snowDepth,totPrecp,visibility = row
    weatherDic[id] = {'MaxSusWind': maxSusWind, "MaxTemp": maxTemp, "MaxWind": maxWind, "MeanDew": meanDew,
                        "MeanSeaPres": meanSeaPres, "MeanTemp": meanTemp, "MeanWind": meanWind, "MinTemp": minTemp,
                        "SnowDepth": snowDepth, "TotPrecp": totPrecp, "Visibility": visibility}



#print(date.fromordinal(date(2018, 1, 1).toordinal() + 10 - 1))





parsedDic = {}
for i, row in enumerate(parsed_data.values):
    id, dayOfWeek, demand, month, startDate, startStation, time = row
    parsedDic[id] = {'dayOfWeek': dayOfWeek, 'Demand': demand, 'month': month, 'startDate': startDate,
                     'startStation': startStation, 'Time': time}


con = lite.connect('bikeWeatherData.db')
cur = con.cursor()


def create_data():
    cur.execute("DROP TABLE IF EXISTS data")
    s = 'CREATE TABLE data(dayOfWeek Int2,demand Int2,month Int2,startDate VARCHAR(20),'
    s = s + 'startStation Int2,time VARCHAR(15))'
    print(s)
    cur.execute(s)

def create_weather():
    cur.execute("DROP TABLE IF EXISTS weather")
    s = 'CREATE TABLE weather(maxSusWind Float,maxTemp Float,maxWind Float,meanDew Float,meanSeaPres Float,'
    s = s + 'meanTemp Float,meanWind Float,minTemp Float, snowDepth Float,totalPrec float, visibility float, startDate VARCHAR(20))'
    print(s)
    cur.execute(s)

def populate_parsedData(data):
    i = 0
    for row in data:
        i = i + 1
        try:
            cur.execute("INSERT INTO data VALUES (?,?,?,?,?,?)",
                        (row['dayOfWeek'], row['demand'], row['month'],
                         str(row['startDate'])[:-3], row['startStation'], row['time']))
        except lite.OperationalError as err:
            print("insert error: %s", err)
        if i % 100 == 0:
            print("inserted row ", str(i))
            con.commit()
    return i


def populate_weatherData(data):
    i = 0
    for row in data:
        i = i + 1
        full_date = date.fromordinal(date(2018, 1, 1).toordinal() + i - 1)

        try:
            cur.execute("INSERT INTO data VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                        (row['maxSusWind'], row['maxTemp'], row['maxWind'],
                         row['meanDew'], row['meanSeasPres'], row['meanTemp'], row['meanWind'], row['minTemp'],
                         row['snowDepth'], row['totPrecp'], row['visibility'], full_date))
        except lite.OperationalError as err:
            print("insert error: %s", err)
        if i % 100 == 0:
            print("inserted row ", str(i))
            con.commit()
    return i


#create_data()
#create_weather()
populate_parsedData(parsedDic)
populate_weatherData(weatherDic)

cur.execute("select * from data")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute("select * from weather")
rows = cur.fetchall()
for row in rows:
    print(row)

#count = 0;


#merged = parsed_data.join(X)

#merged.to_csv("./mergedData.csv")
'''
while count < 5 :      #12671
    Y = parsed_data.iloc[count, :]

    dataTog = {'parsedData': Y, 'weatherData': X}
    df = pd.DataFrame(data=dataTog)

    with open('mergedData.csv', 'a') as fd:
        df.to_csv(fd, header=False)
    print(count)
    #merged = Y.join(X) #neeed to get to string
    count = count + 1
print("out of loop")



'''