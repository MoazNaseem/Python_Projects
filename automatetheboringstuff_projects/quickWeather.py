#! /usr/bin/python3
# quickWeather.py - Prints the weather for a location from the command line.

import sys, json, requests

# Compute location from command line argument.
name = input('Enter the name of the city: ')
name = name[0].upper() + name[1:]
country = input('Enter the appriviation of the country: ').upper()

# Read the city.list.json file
fileObj = open('/home/mizo/Downloads/city.list.json', 'r')
content = fileObj.read()
content = json.loads(content)

# Find the ID of the location.
for i in range(len(content)):
    if content[i]['name'] == name and content[i]['country'] == country:
        cityId = content[i]['id']
# Donwload the Json data from opneweathermap.org's API
url = f'http://api.openweathermap.org/data/2.5/forecast?id={cityId}&appid=a96791edc2b92d0b17432dcb36135468'
response = requests.get(url)
response.raise_for_status()
weatherData = json.loads(response.text)
print()
print(f'Current weather in {name}')
print(weatherData['list'][0]['weather'][0]['main'], '-', weatherData['list'][0]['weather'][0]['description'])
print()
print('Towmorrow:')
print(weatherData['list'][1]['weather'][0]['main'], '-', weatherData['list'][1]['weather'][0]['description'])
print()
print('Day after Towmorrow:')
print(weatherData['list'][2]['weather'][0]['main'], '-', weatherData['list'][1]['weather'][0]['description'])
print()
