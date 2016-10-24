from bs4 import BeautifulSoup
import requests
from pandas import Series,DataFrame
import urllib.request, urllib.error, urllib.parse
import pandas as pd
import naivebayes


def gunosy_train(obj):

	url = "https://gunosy.com/"
	result = requests.get(url)
	c = result.content.decode('utf-8')
	soup = BeautifulSoup(c,"lxml")
	categoryul = soup.find("ul",{'class':'nav_list gtm-click'})

	url = []

	categoryurl = []
	categoryname = []
	categorynum = 0;

	for cat in categoryul:
		if categorynum != 0 and categorynum != 9:
			categoryurl.append(cat.a.get("href"))
			categoryname.append(cat.a.string)
		categorynum = categorynum + 1



	for (url,name) in zip(categoryurl,categoryname):
		result1 = requests.get(url)
		c1 = result1.content.decode('utf-8')
		soup1 = BeautifulSoup(c1,"lxml")
		categorydiv = soup1.find_all("div",class_= 'list_title')
		for categorya in categorydiv:
			title = categorya.a.string
			print("obj.train(%s,%s)" %(title,name))
			obj.train(title,name)


   
    