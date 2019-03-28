#! /usr/bin/python3
# lucky.py automatically opens a browser with
# all the top search results in new tabs

import sys, requests, webbrowser, bs4

if len(sys.argv) < 2:
	print('Usage: ./lucky.py <search Keyword>')
keyword = ' '.join(sys.argv[1:])
res = requests.get('https://www.google.com/search?q=' + keyword)
res.raise_for_status()		# sanity check

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('cite')
numOpen = len(linkElems)
for i in range(numOpen + 1):
	webbrowser.open(linkElems[i].getText())