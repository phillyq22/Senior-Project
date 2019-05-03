from BikeAlg import *
from Station import *
from EndLocation import *
from DisPair import *
from SugPair import *
#pip install geopy

s1 = Station(id = '1', capacity = 16, longitude = -77.0532,latitude = 38.8589, demand = 0, bikeAvail = 2, docAvail = 14)
s2 = Station(id = '2', capacity = 16, longitude = -77.0533,latitude = 38.8572, demand = 0, bikeAvail = 4, docAvail = 12)
s3 = Station(id = '3', capacity = 16, longitude = -77.0492,latitude = 38.8564, demand = 0, bikeAvail = 8, docAvail = 8)
s4 = Station(id = '4', capacity = 16, longitude = -77.0495,latitude = 38.8601, demand = 0, bikeAvail = 2, docAvail = 13)
s5 = Station(id = '5', capacity = 16, longitude = -77.0594,latitude = 38.8578, demand = 0, bikeAvail = 5, docAvail = 15)
s1.prop = .5
s2.prop = .5
s3.prop = .5
s4.prop = .5
s5.prop = .5


dic = {'1':s1, '2':s2, '3':s3, '4':s4, '5':s5}
sl = list(dic.values())

ba = BikeAlg(1)
loc = EndLocation(-77.0512, 38.8588)
d = 1
ba.preProcess(sl, loc)
ba.getSuggest(loc, 0)
print("Stations within: " + str(d) + " miles");
print()
print("Ordered by ascending distance")
i = 0

while(i < ba.getWithin(loc)):
    print(loc.sortedAdj[i])
    i+=1
print()
print("Ordered by descending priority")
for i in range(len(loc.sortedSug)):
    print(loc.sortedSug[i])


