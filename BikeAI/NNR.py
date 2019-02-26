from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.model_selection import train_test_split as tts

df = pd.read_csv('parsedData/Parsed2012Q1.csv')
X = df.iloc[:, :-1]
Y = df.iloc[:, -1]
x_train, x_test, y_train, y_test = tts(X, Y, test_size=0.2)

rf = RandomForestRegressor(n_estimators=1000, random_state=42)
rf.fit(X=x_train, y=y_train)
result = rf.predict(X=x_test)
print(result)
