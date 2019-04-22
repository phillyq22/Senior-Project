# Zac Capell
# 4/5/19
# Senior Project

import json
import statistics
from collections import Counter


def scorer(path):
    avail = []
    ratio = []
    with open(path) as json_file:
        data = json.load(json_file)
        for p in data:
            ratio.append(p["bikeAvail"] / p["docAvail"])
            avail.append(p["bikeAvail"])
        print("Average bike proportion: " + str(round(statistics.mean(ratio) * 100, 2)) + "%")
        print("Maximum bikes available: " + str(max(avail)))
        print("Minimum bikes available: " + str(min(avail)))
        histogram(ratio)


def histogram(inp):
    count = Counter(inp)
    for i in sorted(count):
        print('{0:5f} {1}'.format(round(i * 100, 2), '+' * count[i]))


scorer("data.txt")

