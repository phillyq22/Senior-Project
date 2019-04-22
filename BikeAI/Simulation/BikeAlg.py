from geopy.distance import great_circle
from DisPair import *
from SugPair import *


class BikeAlg:
    def __init__(self):
        self.stationList = []

    def preProcess(self, stationList, loc):
        self.stationList = stationList
        size = len(stationList)
        for i in range(size):
            stationLoc = (stationList[i].longitude, stationList[i].latitude)
            endLoc = (loc.x, loc.y)
            dist = great_circle(stationLoc, endLoc).miles
            # create pair and store at sortedAdjacentIDs[j]
            pair = DisPair(stationList[i], dist)
            loc.sortedAdj.append(pair)
        #sort sortedAdj for location
        loc.sortedAdj.sort()

    def getSuggest(self, loc, dist):

        size = len(loc.sortedAdj)
        i = 0
        while i < size and loc.sortedAdj[i].dist <= dist:
            sug = loc.sortedAdj[i].prio*10 + loc.sortedAdj[i].station.nec*10*loc.sortedAdj[i].station.nec*(10)
            sp = SugPair(loc.sortedAdj[i].station, sug)
            #test distance s.sortedAdj.get(i).dis
            loc.sortedSug.append(sp)
            i+=1
        # reverse order sort
        loc.sortedSug.sort(reverse = True)

    def getWithin(self, loc, dist):
        i = 0
        size = len(loc.sortedAdj)
        while(i < size and loc.sortedAdj[i].dist < dist):
            i+=1
        return i