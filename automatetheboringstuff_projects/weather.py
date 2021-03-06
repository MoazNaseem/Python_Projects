#! /usr/bin/python3
# weather.py opens by default the local weather when I run it
# or accepts command line with the city or country name.

import sys
import pyperclip
import webbrowser

# my city by default
city = 'debrecen'
if len(sys.argv) > 1:
    city = ' '.join(sys.argv[1:])
webbrowser.open_new('https://www.google.com/search?q=weather+' + city)
