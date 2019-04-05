import json

class User:
    def __init__(self, startStation, endStation, endLocation, endDateTime, jsonText=-1):

        if jsonText != -1:
            self.__dict__ = json.loads(jsonText)

        else:
            self.startStation = startStation
            self.endStation = endStation
            self.endLocation = endLocation
            self.endDateTime = endDateTime




