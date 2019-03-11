from pandas import *
import pickle

reg = pickle.load( open( "file", "rb"))
dic = {'Unnamed:' : [1],  'DayOfWeek' : [2], 'Month' : [3],  'StartStation' : [31909],  'Time': [300]}
newdf = DataFrame(data=dic)

print(reg.predict(newdf).round())