from bs4 import BeautifulSoup
import urllib2

def get_soup(url):
	try:
		page = urllib2.urlopen(url)
		soup = BeautifulSoup(page.read(), "html.parser")
		return soup
	except:
		return None;

def amazon_images(url):
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive',}
	request = urllib2.Request(url, headers=hdr)
	page = urllib2.urlopen(request)
	soup = BeautifulSoup(page.read(), "html.parser")
	page.close()
	images = []
	skip_these = ['.gif', 'icon', 'facebook', 'instagram', 'twitter', 'tumblr', 'tumbler', 'pinterest', 'email',]

	for tag in soup.find_all('img', {"src":True}):
		if "/ecx.images" in tag['src']:
			# if '.gif' in tag['src']:
			if any(word in tag['src'].lower() for word in skip_these):
				continue
			elif tag.has_attr('width'):
				if tag['width'].encode('utf-8') > 240:
					images.append(tag['src'].encode('utf-8'))
			elif tag.has_attr('height'):
				if tag['height'] .encode('utf-8') > 100:
					images.append(tag['src'].encode['utf-8'])
			else:
				images.append(tag['src'].encode('utf-8'))

	return images

def gen_images(url):
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive',}
	request = urllib2.Request(url, headers=hdr)
	page = urllib2.urlopen(request)
	soup = BeautifulSoup(page.read(), "html.parser")
	page.close()
	images = []
	skip_these = ['.gif', 'icon', 'facebook', 'instagram', 'twitter', 'tumbler', 'pinterest',]

	for tag in soup.find_all('img', {"src":True}):
		if any(word in tag['src'].lower() for word in skip_these):
			continue
		if tag.has_attr('width'):
			if tag['width'].encode('utf-8') > 100:
				images.append(tag['src'].encode('utf-8'))
		elif tag.has_attr('height'):
			if tag['height'] .encode('utf-8') > 100:
				images.append(tag['src'].encode['utf-8'])
		else:
			images.append(tag['src'].encode('utf-8'))

	return images;

def gen_title(url):
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive',}
	request = urllib2.Request(url, headers=hdr)
	page = urllib2.urlopen(request)
	soup = BeautifulSoup(page.read(), "html.parser")
	page.close()
	return soup.title.string.encode('ascii','ignore')
