#! /usr/bin/python3
# pexelsDownloader.py opens the webbrowser and goes
# to pexels.com and made a search with a keyword you 
# provide and then download the first 100 photos in the
# search result page to a folder with the same keyword.

import datetime, requests, os
from bs4 import BeautifulSoup

seed = datetime.datetime.now().strftime('%Y-%m-%d%%2B%H%%3A%M%%3A%S%%2B%%2B0000')
keyword = input('Enter a search keyword: ')
# wait = ui.WebDriverWait(driver, 10)
url = 'https://www.pexels.com/search/{}/?format=js&seed={}&page='.format(keyword, seed)
headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"}
res = requests.get(url + '1', headers=headers)
pages = int(res.text[res.text.find('totalPages')+11:res.text.find(',',res.text.find('totalPages')+11)])
print('Number of pages: ' + str(pages))
imgurls = []
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
# tagObj = soup.select('.photo-item__img')
if not pages:
	print('Sorry, no pictures found!')
else:
	# print(len(tagObj))
	os.makedirs(str(keyword), exist_ok=True)
	for page in range(1, pages+1):
		imgs = res.text.split('infiniteScrollingAppender.append')[1:]
		for img in imgs:
			soup = BeautifulSoup(img[2:-5].replace("\\'", "'").replace('\\"', '"'), 'html.parser')
			imgurls.append(soup.select('.photo-item__img')[0].get('srcset'))
		if page < pages:
			res = requests.get(url + str(page+1), headers=headers)
		print('Downloading page %s...' %page)
	print('Number of images: ' + str(len(imgurls)))
	for imgurl in imgurls:
			print('Downloading img %s' %imgurl)
			res = requests.get(imgurl, headers=headers)
			res.raise_for_status()
			# print(os.path.basename(comicUrl))
			# open img file for binary writing.
			imgFile = open(os.path.join(str(keyword), os.path.basename(imgurl)), 'wb')
			for chunk in res.iter_content(100000):
				imgFile.write(chunk)
			imgFile.close()
print('Done.')