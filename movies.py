'''
create a model that uses an external api related to movies
'''

import requests
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def main():
    #get the data from the api
    response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=k_mq4vgbc8&language=en-US&page=1")
    data = response.json()
    print("data", data)
    #create a dataframe from the data
    '''df = pd.DataFrame(data)
    #create a new dataframe with only the columns we want
    df = df[["id", "title", "popularity"]]
    #create a new column that is the difference between positiveIncrease and deathIncrease
    df["difference"] = df["id"] - df["popularity"]
    #create the model
    model = LinearRegression()
    print("model created")
    #split the data into training and testing data
    print("splitting data")
    X_train, X_test, y_train, y_test = train_test_split(df[["id", "popularity"]], df["difference"], test_size=0.2)
    print("data split")
    #train the model
    model.fit(X_train, y_train)
    print("model trained")
    #print the score
    print(model.score(X_test, y_test))
    print("score printed")
    #predict the difference for a given positiveIncrease and deathIncrease
    print(model.predict([[100000, 1000]]))'''


if __name__ == "__main__":
    main()


