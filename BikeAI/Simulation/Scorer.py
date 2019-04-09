# Zac Capell
# 4/5/19
# Senior Project

import json
import statistics


class Scorer:
    def scorer(self, path):
        avail = [];
        with open(path) as json_file:
            data = json.load(json_file)
            for p in data:
                avail.append(p["bikeAvail"])
            return statistics.pstdev(avail)

print(Scorer().scorer('StationJson/data.json'))