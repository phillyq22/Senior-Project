from BikeAlg import *
from Station import *
from EndLocation import *
from DisPair import *
from SugPair import *

class DisPair:
    def __init__(self, station, dist, rad):
        self.station = station
        self.dist = dist
        self.rad = rad
        self.prio = rad - dist

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
