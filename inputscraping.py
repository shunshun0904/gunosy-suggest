from bs4 import BeautifulSoup
import requests
import urllib.request, urllib.error, urllib.parse


def url_to_text(url):

	result = requests.get(url)
	c = result.content.decode('utf-8')
	soup = BeautifulSoup(c,"lxml")
	p = soup.h1.string
	return p





	




