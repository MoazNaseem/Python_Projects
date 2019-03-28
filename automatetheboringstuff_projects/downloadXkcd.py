#! /usr/bin/python3
# downloadXkcd.py downloads all the comics in xkcd.com.

import requests, bs4, os

# fix the home page url
url = 'https://xkcd.com'

# make a folder to save the images into.
os.makedirs('xkcd', exist_ok=True)

# make sure your url doesn't end with #, since xkcd.com/1/# is the first page
while not url.endswith('#'):
	print('Downloading page %s...' %url)
	res = requests.get(url)				# get the home page loaded
	res.raise_for_status()				# sanity check

	# bs obj with the page html content
	soup = bs4.BeautifulSoup(res.text, "html.parser")
	tagObj = soup.select('#comic img')
	if tagObj == []:
		print('Couldn\'t find the comic image.')
	else:
		# check src type
		if tagObj[0].get('src').startswith('//imgs.xkcd.com'):
			# forming the comic's url page.
			comicUrl = 'https:' + tagObj[0].get('src')
			print('Downloading image %s...' %comicUrl)
			res = requests.get(comicUrl)			# load the comic's page	
			res.raise_for_status()					# sanity check
			# open img file for binary writing.
			imgFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
			for chunk in res.iter_content(100000):
				imgFile.write(chunk)
			imgFile.close()

			# getting the previous page url
			prevLink = soup.select('a[rel="prev"]')[0]
			url = 'https://xkcd.com' + prevLink.get('href')
		else:
			# getting the previous page url
			prevLink = soup.select('a[rel="prev"]')[0]
			url = 'https://xkcd.com' + prevLink.get('href')

print('Done!')


