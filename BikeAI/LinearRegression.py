from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split as tts
import numpy as np
from progressbar import ProgressBar

pbar = ProgressBar()

data = pd.read_csv('Parsed2012Q1.csv')
X = data.iloc[:, :-1]
Y = data.iloc[:, -1]

x_train, x_test, y_train, y_test = tts(X, Y, test_size=0.2)

reg = LinearRegression().fit(X=x_train, y=y_train)

y_predict = reg.predict(x_test).round()
y_diff = y_test - y_predict

amtWrong = 0

for val in y_diff.values:
    if val > 0:
        amtWrong = amtWrong + 1


testPredDic = {'test': y_test.values, 'predict': y_predict, 'difference': y_diff.values, 'amountWrong': amtWrong}


df = pd.DataFrame(data=testPredDic)
df.to_csv('2012_Q1_LinearRegressionOut.csv')

