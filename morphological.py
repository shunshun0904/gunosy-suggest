#coding: utf-8

import requests
from xml.etree.ElementTree import *

def split(body):
    request_URL = "http://jlp.yahooapis.jp/MAService/V1/parse"

    parameter = {'appid': 'dj0zaiZpPVVKS0lNNk1nVWtZRiZzPWNvbnN1bWVyc2VjcmV0Jng9Y2M-',
                'sentence': body,
                'results': 'ma',
                'filter':'1|2|3|4|5|9|10'}
    r = requests.get(request_URL, params=parameter)

    elem = fromstring(r.text.encode('utf-8'))

    words = []
    for e in elem.getiterator("{urn:yahoo:jp:jlp}surface"):
        words.append(e.text)

    return words





    