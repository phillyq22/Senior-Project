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

