# Zac Capell
# 4/5/19
# Senior Project

import json
import statistics
import matplotlib.pyplot as plt


def scorer(path):
    avail = []
    ratio = []
    with open(path) as json_file:
        data = json.load(json_file)
        for p in data:

            ratio.append(round((p["bikeAvail"] / (p["docAvail"] + p["bikeAvail"])), 2) * 100)
            avail.append(p["bikeAvail"])
        print("Average bike proportion: " + str(statistics.mean(ratio)) + "%")
        print("Maximum bikes available: " + str(max(avail)))
        print("Minimum bikes available: " + str(min(avail)))

        plt.hist(ratio, facecolor='grey', alpha=0.5)
        plt.xlabel("% of Bikes Available")
        plt.ylabel("Number of Stations")
        plt.title("Bike Distribution by Ratio")
        plt.show()
