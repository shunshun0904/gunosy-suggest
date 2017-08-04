# coding: utf-8
# 命名規則： PEP8
# YahooのAPIを利用して形態素解析
import requests
from xml.etree.ElementTree import *
import csv


f = open('vocaburary.csv', 'w')
csvWriter = csv.writer(f)


def split(body):
    request_URL = "http://jlp.yahooapis.jp/MAService/V1/parse"
    parameter = {'appid': """dj00aiZpPUxFRFVpcmx2UnpLNiZ
    zPWNvbnN1bWVyc2VjcmV0Jng9ODc-""",
                 'sentence': body,
                 'results': 'ma',
<<<<<<< HEAD
=======
                 # 'filter': '1|2|3|4|5|9|10'}
>>>>>>> ad263d0b5740e50931d8a7afee75e8495bea1084
                 'filter': '1|2|9|10'}
    r = requests.get(request_URL, params=parameter)

    try:
        elem = fromstring(r.text.encode('utf-8'))

    except BaseException:
        pass
    else:
        words = []
        for e in elem.getiterator("{urn:yahoo:jp:jlp}surface"):
            words.append(e.text)
        csvWriter.writerow(words)
        return words
