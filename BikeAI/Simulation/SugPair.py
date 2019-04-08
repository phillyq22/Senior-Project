from BikeAlg import *
from Station import *
from EndLocation import *
from DisPair import *
from SugPair import *

class SugPair:
    def __init__(self, station, sug):
        self.station = station
        self.sug = sug

    def compare(self, pair):
        if (self.sug - pair.sug > 0):
            return 1
        if (self.sug - pair.sug == 0):
            return 0
        return -1

    def __lt__(self, other):
        return self.sug < other.sug

    def __gt__(self, other):
        return self.sug > other.sug

    def __eq__(self, other):
        return self.sug == other.sug

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "(" + str(self.station.id) + ", " + str(self.sug) + ")"