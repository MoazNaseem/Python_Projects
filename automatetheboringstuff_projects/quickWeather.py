#! /usr/bin/python3
# quickWeather.py - Prints the weather for a location from the command line.

import sys
import json
import requests


def output_info(weatherData):
    print(f'Current weather in {cityName}')
    print(weatherData['list'][0]['weather'][0]['main'], '-', weatherData['list'][0]['weather'][0]['description'])
    print()
    print('Towmorrow:')
    print(weatherData['list'][1]['weather'][0]['main'], '-', weatherData['list'][1]['weather'][0]['description'])
    print()
    print('Day after Towmorrow:')
    print(weatherData['list'][2]['weather'][0]['main'], '-', weatherData['list'][1]['weather'][0]['description'])
    print()


def get_page(cityId):
    # Donwload the Json data from opneweathermap.org's API
    url = f'http://api.openweathermap.org/data/2.5/forecast?id={cityId}&appid=a96791edc2b92d0b17432dcb36135468'
    with requests.get(url) as response:
        weatherData = json.loads(response.text)
    output_info(weatherData)


def find_city_id(content):
    # Find the ID of the location.
    for i in range(len(content)):
        if content[i]['name'] == cityName and content[i]['country'] == country:
            cityId = content[i]['id']
    get_page(cityId)


def read_city_list():
    # find the location in city.list.json file
    with open('./city.list.json', 'r') as fileObj:
        content = fileObj.read()
        content = json.loads(content)
    find_city_id(content)


def get_location():
    # Prompt the usr for the location.
    cityName = input('Enter the name of the city: ').capitalize()
    country = input('Enter the appriviation of the country: ').upper()
    return cityName, country


if __name__ == '__main__':
    cityName, country = get_location()
    read_city_list()
