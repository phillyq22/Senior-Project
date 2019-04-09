from BikeAlg import *
from Station import *
from EndLocation import *
from DisPair import *
from SugPair import *


s1 = Station(1, 1, -77.0532, 38.8589, .9, 1, 1)
s2 = Station(2,  1,-77.0533, 38.8572, .5, 1, 1)
s3 = Station(3,  1,-77.0492, 38.8564, .5, 1, 1)
s4 = Station(4,  1,-77.0495, 38.8601, .7, 1, 1)
s5 = Station(5,  1,-77.0594, 38.8578, .2, 1, 1)
sl = [s1,s2,s3,s4,s5]
ba = BikeAlg()
loc = EndLocation(-77.0512, 38.8588)
d = 0.3 #5
ba.preProcess(sl, loc)
ba.getSuggest(loc, d)
print("Stations within: " + str(d) + " miles");
print()
print("Ordered by ascending distance")
i = 0
while(i < ba.getWithin(loc,d)):
    print(loc.sortedAdj[i])
    i+=1
print()
print("Ordered by descending priority")
for i in range(len(loc.sortedSug)):
    print(loc.sortedSug[i])

