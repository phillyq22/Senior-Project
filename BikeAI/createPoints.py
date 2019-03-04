import json
import math


json_data = open("reqData.json").read()
json_data = json_data.replace("\'s ", " ")
json_data = json_data.replace("\'E", " ")
json_data = json_data.replace("\'", "\"")
json_data = json_data.replace(": ", ":\"")
json_data = json_data.replace("False", "\"False\"")
json_data = json_data.replace("True", "\"True\"")
json_data = json_data.replace("None", "\"None\"")

data = json.loads(json_data)


class PointGeometry:
    def __init__(self, stationId, x, y):
        self.stationId = stationId
        self.x = x
        self.y = y

    def toString(self):
        return "ID: " + str(self.stationId) + " x: " + str(self.x) + " y " + str(self.y)

    def calcDistance(self, x, y):
        return math.sqrt((x - self.x)**2 + (y - self.y)**2)



points = []

for feature in data["features"]:
    tempID = feature["attributes"]["ID"]
    tempX = feature["geometry"]["x"]
    tempY = feature["geometry"]["y"]
    points.append(PointGeometry(tempID, tempX, tempY))

for point in points:
    print(point.toString())
    print(point.calcDistance(0, 0))
    print(point.calcDistance(point.x, point.y))

