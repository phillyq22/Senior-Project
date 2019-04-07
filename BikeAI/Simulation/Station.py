import json


class Station:
    def __init__(self, id, name, longitude, latitude, nec, bikeAvail, docAvail, jsonText=-1):

        if jsonText != -1:
            self.__dict__ = json.loads(jsonText)

        else:
            self.id = id
            self.name = name
            self.longitude = longitude
            self.latitude = latitude
            self.nec = nec
            self.bikeAvail = bikeAvail
            self.docSize = bikeAvail + docAvail
            self.docAvail = docAvail

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


