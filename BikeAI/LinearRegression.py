from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split as tts
import numpy as np
import os
import pickle



'''
Reads in the weather data, puts demand variable in Y, puts rest of the relevant variables into X
Change "finalWeatherData.csv" to wherever your data.csv file is
'''
data = pd.read_csv('./finalWeatherData.csv')
X = data.iloc[:, [1, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17]]
Y = data.iloc[:, 2]

'''
Trains the Linear Regression Model
'''
x_train, x_test, y_train, y_test = tts(X, Y, test_size=0.2)
reg = LinearRegression().fit(X=x_train, y=y_train)
y_predict = reg.predict(x_test).round()
y_diff = y_test - y_predict

'''
Calculating the percentage wrong on the training
'''
amtWrong = 0
for val in y_diff.values:
    if val > 0:
        amtWrong = amtWrong + 1
percWrong = (amtWrong / len(y_predict)) *100


'''
Creating the dictionary to input into text file 
test = the values of actual demand
predict = predicted demand from the LinearRegression
difference = the difference between the test values and the predicted demand
amountWrong = the total amount of wrong predictions
percentWrong = percentage of wrong predictions 
'''
testPredDic = {'test': y_test.values, 'predict': y_predict, 'difference': y_diff.values, 'amountWrong': amtWrong,
               'percentWrong': percWrong}

'''
Inputting the values into a CSV
'''
path = 'LinearRegressionOuts'
df = pd.DataFrame(data=testPredDic)
df.to_csv(os.path.join(path, '2018_LinearRegressionOut_weather.csv'))

'''
Creating and exporting the weights for export
'''
eCoeff = reg.intercept_
weights = reg.coef_
score = reg.score(X=x_test, y=y_test)
weightsDic = {'Estimated Coefficient': eCoeff, 'Weights': weights, 'Score': score}

cf = pd.DataFrame(data=weightsDic)
cf.to_csv(os.path.join(path, 'Weights.csv'))

print('Estimated intercept coefficient:', eCoeff)
print('Number of coefficients:', weights)
print('R^2:', score)
with open('file', 'wb') as pickle_file:
    pickle.dump(reg, pickle_file)
#cf = pd.DataFrame(zip(X.columns, reg.coef_), columns=['features', 'estimatedCoefficients'])
#cf.to_csv(os.path.join(path, "model.csv"))



