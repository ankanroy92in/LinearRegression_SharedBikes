# headers
import pandas as pd

def read_dataset():
    # Reading dataset and the name of the data frame is bikes
    bikes = pd.read_csv('day.csv')
    return bikes

# Droping uncessary columns
bikes.drop(['instant','casual','registered','dteday'],axis=1,inplace=True)

# Dummy variable creation
bikes['season'] = bikes['season'].map({1: 'spring', 2:'summer', 3:'fall', 4:'winter'})
bikes['mnth']=bikes.mnth.map({1:'Jan',2:'Feb',3:'Mar',4:'Apr',
                              5:'May',6:'June',7:'July',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'})
bikes['weekday']=bikes.weekday.map({0:'Sun',1:'Mon',2:'Tue',3:'Wed',4:'Thu',5:'Fri',6:'Sat'})
bikes['weathersit']=bikes.weathersit.map({1: 'Clear',2:'Mist + Cloudy',3:'Light Snow',4:'Snow + Fog'})

# Creating dummy variables and drop the columns which is not required like (m-1)*n where m is level 
# and n is category
seasons = pd.get_dummies(bikes['season'], drop_first = True)
month = pd.get_dummies(bikes.mnth,drop_first = True)
weekdays = pd.get_dummies(bikes.weekday,drop_first = True)
weather = pd.get_dummies(bikes.weathersit,drop_first = True)

bikes = pd.concat([bikes,seasons,month,weekdays,weather], axis = 1)

# Dropping the original categorical variable 
bikes.drop(['season','mnth','weekday','weathersit'],axis = 1, inplace = True)

