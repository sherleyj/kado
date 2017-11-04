from bs4 import BeautifulSoup
import urllib2
from urlparse import urlparse

def get_soup(url):
	try:
		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive',}
		request = urllib2.Request(url, headers=hdr)
		page = urllib2.urlopen(request)
		soup = BeautifulSoup(page.read(), "html.parser")
		page.close()
		return soup
	except Exception, e:
		return None
	

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
	
	og_image = soup.find('meta', property="og:image")
	if og_image:
		print "had og_image"
		images.append(og_image['content'].encode('utf-8'))

	for tag in soup.find_all('img', {"src":True}):
		if any(word in tag['src'].lower() for word in skip_these):
			continue
		if tag.has_attr('width'):
			if tag['width'].encode('utf-8') > 100:
				images.append(tag['src'].encode('utf-8'))
		elif tag.has_attr('height'):
			if tag['height'].encode('utf-8') > 100:
				images.append(tag['src'].encode('utf-8'))
		else:
			images.append(tag['src'].encode('utf-8'))

	if not images:
		for tag in soup.find_all('img', {"src":True}):
			images.append(tag['src'].encode('utf-8'))
			print str(soup)

	return images;

def gen_title(url):
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive',}
	request = urllib2.Request(url, headers=hdr)
	page = urllib2.urlopen(request)
	soup = BeautifulSoup(page.read(), "html.parser")
	page.close()

	og_title = soup.find('meta', property="og:title")

	if og_title:
		return og_title['content'].encode('utf-8', 'ignore')

	return soup.title.string.encode('ascii','ignore')

def og_site_name(url):
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive',}
	request = urllib2.Request(url, headers=hdr)
	page = urllib2.urlopen(request)
	soup = BeautifulSoup(page.read(), "html.parser")
	page.close()

	og_site_name = soup.find('meta', property="og:site_name")
	if og_site_name:
		return og_site_name['content'].encode('utf-8', 'ignore')

	return "";

def og_description(url):
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive',}
	request = urllib2.Request(url, headers=hdr)
	page = urllib2.urlopen(request)
	soup = BeautifulSoup(page.read(), "html.parser")
	page.close()

	og_description = soup.find('meta', property="og:description")
	if og_description:
		return og_description['content'].encode('utf-8', 'ignore')

	return "";

def og_shortcut_icon(url):
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive',}
	request = urllib2.Request(url, headers=hdr)
	page = urllib2.urlopen(request)
	soup = BeautifulSoup(page.read(), "html.parser")
	page.close()

	og_shortcut_icon = soup.find('link', rel="icon") 
	purl = urlparse(url)
	domain = purl.netloc
	favicon_addr = ""

	if og_shortcut_icon:
		favicon_addr = og_shortcut_icon['href']
		if domain in favicon_addr:
			favicon_addr = favicon_addr
		else:
			favicon_addr = domain + favicon_addr
	# elif "amazon" in domain:
	# 	return "http://www.amazon.com/favicon.ico"
	else:
		favicon_addr = domain + "/favicon.ico"
	print(favicon_addr)
	return "//" + favicon_addr















