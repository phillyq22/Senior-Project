import json

'''
User object to represent CapitalBikeShare users.
'''
class User:
    def __init__(self, startStation, endStation, endLocation, endDateTime, startLocation, jsonText=-1):

        if jsonText != -1:
            self.__dict__ = json.loads(jsonText)

        else:
            self.startStation = startStation # station bike is picked up from
            self.endStation = endStation # station bike is dropped off
            self.endLocation = endLocation # Where the user departs from to go to end station
            self.endDateTime = endDateTime # Time that the bike is dropped off
            self.startLocation = startLocation # Where the user departs from to go to the start station

    def __str__(self):
        return 'Start Station: ' + str(self.startStation) + ' End Station: ' + str(self.endStation) + ' End Location: ' \
               + str(self.endLocation) + ' End Date Time: ' + str(self.endDateTime)





