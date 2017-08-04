# coding: utf-8
# 命名規則： PEP8
import requests
from xml.etree.ElementTree import *
import csv


f = open('vocaburary.csv', 'w')
csvWriter = csv.writer(f)


def split(body):
    # YahooのAPIを利用して形態素解析
    request_URL = "http://jlp.yahooapis.jp/MAService/V1/parse"
    parameter = {'appid': """dj00aiZpPUxFRFVpcmx2UnpLNiZzPWNvbnN1bWVyc2VjcmV0Jng9ODc-""",
                 'sentence': body,
                 'results': 'ma',
                 # 'filter': '1|2|3|4|5|9|10'}
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
