from json import *
import json


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

'''
Station objects to be used to represent bike stations of CapitalBikeShare.
'''
class Station:
    prop = 0

    def __init__(self, id="null", capacity="null", longitude="null", latitude="null", demand="null", bikeAvail="null", docAvail="null", jsonText='No Json'):

        if jsonText != 'No Json':
            self.__dict__ = json.loads(jsonText)

        else:
            self.id = id # Uniquely identifies a station
            self.capacity = capacity # How many total bikes can fit in this station.
            self.longitude = longitude
            self.latitude = latitude
            self.demand = demand # Number of bikes expected to be needed
            self.bikeAvail = bikeAvail # Number of bikes available
            self.docSize = bikeAvail + docAvail
            self.docAvail = docAvail # Number of available bike docks

    def toJSON(self):
        return self.__dict__

    #def jsonify(self):
        #print(json.dumps(self))

    # Decreases the number of bikes available, but also increases the number of docks available.
    def decreaseBikeAvail(self):
        self.bikeAvail -= 1
        self.increaseDocAvail()

    # Increases the number of bikes available, but also decreases the number of docks available.
    def increaseBikeAvail(self):
        self.bikeAvail += 1
        self.decreaseDocAvail()

    # Decreases the number of docks available at this station.
    def decreaseDocAvail(self):
        self.docAvail -= 1

    # Increases the number of docks available at this station.
    def increaseDocAvail(self):
        self.docAvail += 1

    # Returns whether or not there are bikes available
    def isBikeAvail(self):
        return self.bikeAvail > 0

    # Returns whether or not there are docks available
    def isDocAvail(self):
        return self.docAvail > 0

    # Calculates the necessity of this station. This has to do with the the target bike distribution, bikes available,
    # and demand.
    def calcNec(self, time):
        target = self.prop * self.docSize
        #NO TAAAAHHHMMM
        #return target - (self.bikeAvail - self.demand[time])
        return target - (self.bikeAvail - 0)


