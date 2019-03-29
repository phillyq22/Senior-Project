import matplotlib.pyplot as plt
from numpy import exp, loadtxt, pi, sqrt
import numpy as np

from lmfit import Model


def gaussian(x, amp, cen, wid):
    """1-d gaussian: gaussian(x, amp, cen, wid)"""
    return (amp / (sqrt(2 * pi) * wid)) * exp(-(x - cen) ** 2 / (2 * wid ** 2))

class NormalModel:

    def __init__(self):
        self.result = -1
        self.amp = -1
        self.cen = -1
        self.wid = -1



    def fitModel(self,arrayIn, plotData):
        data = np.array(arrayIn)
        x = data[:, 0]
        y = data[:, 1]
        gmodel = Model(gaussian)
        self.result = gmodel.fit(y, x=x, amp=10, cen=690, wid=1380)

        self.amp = self.result.best_values['amp']
        self.cen = self.result.best_values['wid']
        self.wid = self.result.best_values['wid']

        if plotData:
            print(self.result.fit_report())
            plt.plot(x, y, 'bo')
            plt.plot(x, self.result.init_fit, 'k--')
            plt.plot(x, self.result.best_fit, 'r-')
            plt.show()







