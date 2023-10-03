'''
Create a machine learning model with sklearn that uses an external api
'''

import requests
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def main():
    #get the data from the api
    response = requests.get("https://api.covidtracking.com/v1/us/daily.json")
    data = response.json()
    #create a dataframe from the data
    df = pd.DataFrame(data)
    #create a new dataframe with only the columns we want
    df = df[["positiveIncrease", "deathIncrease"]]
    #create a new column that is the difference between positiveIncrease and deathIncrease
    df["difference"] = df["positiveIncrease"] - df["deathIncrease"]
    #create the model
    model = LinearRegression()
    #split the data into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(df[["positiveIncrease", "deathIncrease"]], df["difference"], test_size=0.2)
    #train the model
    model.fit(X_train, y_train)
    #print the score
    print(model.score(X_test, y_test))
    #predict the difference for a given positiveIncrease and deathIncrease
    print(model.predict([[100000, 1000]]))