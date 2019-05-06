from BikeAlg import *
from Station import *
from EndLocation import *
from DisPair import *
from SugPair import *

#Custom Data Structure to match stations with distances
class DisPair:
    def __init__(self, station, dist, rad):
        self.station = station
        #Distance between given station and end location
        self.dist = dist
        #Algorithm looks at stations within radius 'rad'
        self.rad = rad
        #Used for necessity equation (Trying to weigh distance)
        self.prio = (rad - dist)/rad

#Custom compare function for sorting
    def compare(self, pair):
        if (self.dist - pair.dist > 0):
            return 1
        if (self.dist - pair.dist == 0):
            return 0
        return -1

    def __lt__(self, other):
        return self.dist < other.dist

    def __gt__(self, other):
        return self.dist > other.dist

    def __eq__(self, other):
        return self.dist == other.dist

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "(" + str(self.station.id) + ", " + str(self.dist) + ")"
