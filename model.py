'''
Create a function that reuqests an api
'''

import requests
import json

def get_data():
    '''
    Request data from api
    '''
    url = 'https://api.covid19api.com/summary'
    response = requests.get(url)
    data = response.json()
    return data

def get_country_data(country):
    '''
    Request data from api
    '''
    url = 'https://api.covid19api.com/total/country/' + country
    response = requests.get(url)
    data = response.json()
    return data


def main():
    get_data()
    get_country_data('mexico')

if __name__ == '__main__':
    main()