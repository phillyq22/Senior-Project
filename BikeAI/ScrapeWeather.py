from pandas import *
import json
import time
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import rrule

weatherDic = {'MinTemp': [], 'MeanTemp': [], 'MaxTemp': [], 'MeanSeaPreassure': [], 'MeanDew': [],
              'TotalPrecpitation': [], 'Visibility': [], 'SnowDepth': [], 'MeanWind': [], 'MaxSustainedWind': [],
              'MaxWind': []}

startDay = datetime(2018, 1, 1)
endYear = datetime(2019, 1, 1)

worked = False
for dt in rrule.rrule(rrule.DAILY, dtstart=startDay, until=endYear):
    worked = False
    while worked == False:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
            reg_url = "https://www.almanac.com/weather/history/zipcode/19019/" + str(dt.year) + "-" + str(dt.month) + "-" + str(
                dt.day)
            req = Request(url=reg_url, headers=headers)
            html = urlopen(req).read()

            soup = BeautifulSoup(html, features="html.parser")

            # print(soup)
            filter1 = soup.findAll(["span", "p"], {"class": ["value", "nullvalue"]})

            results = filter1

            cleanList = []
            for result in results:
                itemToAdd = str(result)[20:-7]
                if itemToAdd == '>No da':
                    itemToAdd = "0"
                cleanList.append(itemToAdd)

            weatherDic['MinTemp'].append(cleanList[0])
            weatherDic['MeanTemp'].append(cleanList[1])
            weatherDic['MaxTemp'].append(cleanList[2])
            weatherDic['MeanSeaPreassure'].append(cleanList[3])
            weatherDic['MeanDew'].append(cleanList[4])
            weatherDic['TotalPrecpitation'].append(cleanList[5])
            weatherDic['Visibility'].append(cleanList[6])
            weatherDic['SnowDepth'].append(cleanList[7])
            weatherDic['MeanWind'].append(cleanList[8])
            weatherDic['MaxSustainedWind'].append(cleanList[9])
            weatherDic['MaxWind'].append(cleanList[10])

            print(str(dt) + " Done!")

            time.sleep(3)
            worked = True
        except:
            print("request error")
            time.sleep(10)

#print(weatherDic)
newdf = DataFrame(data=weatherDic)

newdf.to_csv('WeatherData.csv')