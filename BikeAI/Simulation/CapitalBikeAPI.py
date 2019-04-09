import requests
from datetime import datetime
import sqlite3 as lite

'''
Allows for creation and connection to the bikeAPI database.

'''
class CapitalBikeApi:

    def __init__(self):
        self.con = lite.connect('bikeAPI.db')
        self.cur = self.con.cursor()
        self.create_station_status()
        self.create_stations()
        self.populate_stations(self.get_stations_from_api())
        self.populate_station_status(self.get_station_status_from_api())

    def create_station_status(self):
        self.cur.execute("DROP TABLE IF EXISTS station_status")
        s = 'CREATE TABLE station_status(stationID VARCHAR(8),bikesAvailable Int2,ebikesAvailable Int2,bikesDisabled Int2,'
        s = s + 'docksAvailable Int2,docksDisabled Int2,isInstalled Int2,isRenting Int2, isReturning Int2, date DATETIME)'
        print(s)
        self.cur.execute(s)

    def create_stations(self):
        self.cur.execute("DROP TABLE IF EXISTS stations")
        s = 'CREATE TABLE stations(stationID VARCHAR(8),capacity Int2,regionID Int2,latitude float,longitude float,'
        s = s + 'name VARCHAR(50),shortName VARCHAR(8))'
        print(s)
        self.cur.execute(s)

    def get_station_status_from_api(self):
        ''' Get data from api.
            Make sure to return data, last_updated, and ttl '''
        url = 'https://gbfs.capitalbikeshare.com/gbfs/en/station_status.json'
        response = requests.get(url)
        # if response is not good, raise error
        response.raise_for_status()
        return response.json()

    def get_stations_from_api(self):
        ''' Get data from api.
            Make sure to return data, last_updated, and ttl '''
        url = 'https://gbfs.capitalbikeshare.com/gbfs/en/station_information.json'
        response = requests.get(url)
        # if response is not good, raise error
        response.raise_for_status()
        return response.json()

    def populate_station_status(self, data):
        i = 0
        for row in data["data"]["stations"]:
            i = i + 1
            ts = int(row["last_reported"])
            ts = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            try:
                self.cur.execute("INSERT INTO station_status VALUES (?,?,?,?,?,?,?,?,?,?)",
                            (row['station_id'], row['num_bikes_available'], row['num_ebikes_available'],
                             row['num_bikes_disabled'], row['num_docks_available'], row['num_docks_disabled'],
                             row['is_installed'], row['is_renting'], row['is_returning'], ts))
            except lite.OperationalError as err:
                print("insert error: %s", err)
            if i % 100 == 0:
                print("inserted row ", str(i))
                self.con.commit()
        return i

    def populate_stations(self, data):
        i = 0
        for row in data["data"]["stations"]:
            i = i + 1
            try:
                self.cur.execute("INSERT INTO stations VALUES (?,?,?,?,?,?,?)",
                            (row['station_id'], row['capacity'], row['region_id'], row['lat'], row['lon'],
                             row['name'], row['short_name']))
            except lite.OperationalError as err:
                print("insert error: %s", err)
            if i % 100 == 0:
                print("inserted row ", str(i))
                self.con.commit()
        return i

    def create_simulation_json(self):
        self.cur.execute("select shortName, longitude, latitude, bikesAvailable, capacity, docksAvailable, 'NAN' as nec from station_status join stations using(stationID)")
        rows = self.cur.fetchall()
        data = {}
        data['stations'] = []

        for row in rows:
            data['stations'].append({'id': row[0], 'longitude': row[1], 'latitude': row[2], 'bikeAvail': row[3],
                                     'capacity': row[4], 'docAvail': row[5], 'nec': row[6]})
        return data

    def get_cur(self):
        return self.cur

    def execute_sql(self, sql):
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)


'''
STUFF USED TO DO TESTING:

create_station_status()

cur.execute("select * from station_status")
rows = cur.fetchall()
for row in rows:
    print(row)


numRows = populate_station_status(get_station_status_from_api())
currTime = dt.datetime.now()
with open('dataRecord.txt', 'a') as file:
    file.write(str(numRows) + ', ' + str(currTime) + '\n')


create_stations()

populate_stations(get_stations_from_api())
cur.execute("select * from stations")
rows = cur.fetchall()
for row in rows:
    print(row)


#Write your sql query here. stations and station_status are the two tables
cur.execute("select * from station_status join stations using(stationID) where bikesAvailable = 0")
rows = cur.fetchall()
for row in rows:
    print(row)
'''
