from json import *
import json


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Station:
    prop = 0

    def __init__(self, id="null", capacity="null", longitude="null", latitude="null", demand="null", bikeAvail="null", docAvail="null", jsonText='No Json'):

        if jsonText != 'No Json':
            self.__dict__ = json.loads(jsonText)

        else:
            self.id = id
            self.capacity = capacity
            self.longitude = longitude
            self.latitude = latitude
            self.demand = demand
            self.bikeAvail = bikeAvail
            self.docSize = bikeAvail + docAvail
            self.docAvail = docAvail

    def toJSON(self):
        return self.__dict__

    #def jsonify(self):
        #print(json.dumps(self))


    def decreaseBikeAvail(self):
        self.bikeAvail -= 1
        self.increaseDocAvail()

    def increaseBikeAvail(self):
        self.bikeAvail += 1
        self.decreaseDocAvail()

    def decreaseDocAvail(self):
        self.docAvail -= 1

    def increaseDocAvail(self):
        self.docAvail += 1

    def isBikeAvail(self):
        return self.bikeAvail > 0

    def isDocAvail(self):
        return self.docAvail > 0

    def calcNec(self, time):
        target = self.prop * self.docSize
        return target - (self.bikeAvail - self.demand[time])


