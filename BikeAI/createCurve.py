import matplotlib.pyplot as plt
from numpy import exp, loadtxt, pi, sqrt
import numpy as np

from lmfit import Model

data = np.array([[0,3],[1,4],[2,8],[5,8],[6,2]])
x = data[:, 0]
y = data[:, 1]


def gaussian(x, amp, cen, wid):
    """1-d gaussian: gaussian(x, amp, cen, wid)"""
    return (amp / (sqrt(2*pi) * wid)) * exp(-(x-cen)**2 / (2*wid**2))


gmodel = Model(gaussian)
result = gmodel.fit(y, x=x, amp=3, cen=3, wid=7)


print(result.fit_report())

print('Predicted value: ' , gaussian(4,result.best_values['amp'],result.best_values['cen'],result.best_values['wid']))

plt.plot(x, y, 'bo')
plt.plot(x, result.init_fit, 'k--')
plt.plot(x, result.best_fit, 'r-')
plt.show()

