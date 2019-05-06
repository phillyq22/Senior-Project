'''
End location object to represent the desired destination of a bike share user.
Utilized in simulation. End locations are randomly generated within a radius of the end station.
'''
class EndLocation:
    def __init__(self, x, y):
        self.name = ''
        self.x = x # longitude
        self.y = y # latitude
        self.sortedAdj = []
        self.sortedSug = []
