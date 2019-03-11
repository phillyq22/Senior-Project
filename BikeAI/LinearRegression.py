from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split as tts
import numpy as np
from progressbar import ProgressBar
import os
import pickle

pbar = ProgressBar()

data = pd.read_csv('./parsedData/Parsed2018_withzero.csv')
X = data.iloc[:, [0, 1, 3, 4, 5]]
Y = data.iloc[:, 2]

x_train, x_test, y_train, y_test = tts(X, Y, test_size=0.2)

reg = LinearRegression().fit(X=x_train, y=y_train)

y_predict = reg.predict(x_test).round()

y_diff = y_test - y_predict

amtWrong = 0

for val in y_diff.values:
    if val > 0:
        amtWrong = amtWrong + 1

percWrong = (amtWrong / len(y_predict)) *100


testPredDic = {'test': y_test.values, 'predict': y_predict, 'difference': y_diff.values, 'amountWrong': amtWrong,
               'percentWrong': percWrong}

path = 'LinearRegressionOuts'

df = pd.DataFrame(data=testPredDic)
df.to_csv(os.path.join(path, '2018_LinearRegressionOutEC2.csv'))

eCoeff = reg.intercept_
weights = reg.coef_
weightsDic = {'Estimated Coefficient': eCoeff, 'Weights': weights}

cf = pd.DataFrame(data=weightsDic)
cf.to_csv(os.path.join(path, 'Weights.csv'))

print('Estimated intercept coefficient:', reg.intercept_)
print('Number of coefficients:', reg.coef_)

with open('file', 'wb') as pickle_file:
    pickle.dump(reg, pickle_file)
#cf = pd.DataFrame(zip(X.columns, reg.coef_), columns=['features', 'estimatedCoefficients'])
#cf.to_csv(os.path.join(path, "model.csv"))



