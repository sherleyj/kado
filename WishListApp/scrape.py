from bs4 import BeautifulSoup
import urllib2

def amazon_images(url):
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read(), "html.parser")

	images = []

	for tag in soup.find_all('img'):
		if "/ecx.images" in tag['src']:
			if tag.has_attr('width') or tag.has_attr('height'):
				if tag['width'].encode('utf-8') > 100 or tag['height'].encode('utf-8') > 100:
					images.append(tag['src'].encode('utf-8')) 
			else:
				images.append(tag['src'].encode('utf-8'))

	return images

def gen_images(url):
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read(), "html.parser")
	images = []

	for tag in soup.find_all('img'):
		if tag.has_attr('width') or tag.has_attr('height'):
			if int(tag['width']) > 100 or int(tag['height']) > 100:
				images.append(tag['src'].encode('utf-8'))
		else:
			images.append(tag['src'].encode('utf-8'))

	return images;

def gen_title(url):
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read(), "html.parser")
	return soup.title.string.encode('ascii','ignore')
