from geopy.distance import great_circle
from DisPair import *
from SugPair import *


class BikeAlg:
    def __init__(self, rad):
        self.stationList = []
        self.rad = rad

#Creates a list of DisPairs between a location and all stations stored in 'loc'
    def preProcess(self, stationList, loc):
        self.stationList = stationList
        size = len(stationList)
        for i in range(size):
            stationLoc = (stationList[i].longitude, stationList[i].latitude)
            endLoc = (loc.x, loc.y)
            dist = great_circle(stationLoc, endLoc).miles
            # create pair and store at sortedAdjacentIDs[j]
            pair = DisPair(stationList[i], dist, self.rad)
            loc.sortedAdj.append(pair)
        #sort sortedAdj for location
        loc.sortedAdj.sort()

#Creates a list of SugPairs between a location and all stations stored in 'loc'
    def getSuggest(self, loc, time):

        size = len(loc.sortedAdj)
        i = 0
        while i < size and loc.sortedAdj[i].dist <= self.rad:
            #Equation for balancing (Subject to change)
            sug = loc.sortedAdj[i].prio*10*loc.sortedAdj[i].prio*10 + loc.sortedAdj[i].station.calcNec(time)*10
            sp = SugPair(loc.sortedAdj[i].station, sug)
            #test distance s.sortedAdj.get(i).dis
            loc.sortedSug.append(sp)
            i += 1
        # reverse order sort
        loc.sortedSug.sort(reverse = True)

#Returns index of number of stations within given range, used with sortedAdj in EndLocation to return all stations within radius
    def getWithin(self, loc):
        i = 0
        size = len(loc.sortedAdj)
        while(i < size and loc.sortedAdj[i].dist < self.rad):
            i+=1
        return i
