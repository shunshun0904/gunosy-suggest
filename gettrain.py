# 命名規則： PEP8
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import naivebayes
#import naivebayes_normal
import time
import csv


def gunosy_train(obj):

    # カテゴリーのurl
    categories = {
        'https://gunosy.com/categories/1': 'エンタメ',
        'https://gunosy.com/categories/2': 'スポーツ',
        'https://gunosy.com/categories/3': 'おもしろ',
        'https://gunosy.com/categories/4': '国内',
        'https://gunosy.com/categories/5': '海外',
        'https://gunosy.com/categories/6': 'コラム',
        'https://gunosy.com/categories/7': 'IT・科学',
        'https://gunosy.com/categories/8': 'グルメ',
    }

    # 各カテゴリー内のページのタイトルインデックス(定数)
    PAGE_TITLE_START = 0
    PAGE_TITLE_END = 20

    # 各カテゴリー内のページの枚数の番号（定数）
    # 汎用性を持たせるため値は変更可能。ただし、1<=CATEGORY_START,CATEGORY_END<=100
    CATEGORY_START = 1
    CATEGORY_END = 100

    # 取得ページ数の表示
    page_numbers = 1

    f = open('subject.csv', 'w')
    csvWriter = csv.writer(f)
    f = open('category.csv', 'w')
    csvWriter2 = csv.writer(f)
    for url, name in categories.items():
        # try文でカプセル化します。
        # 各カテゴリーのhtmlを取得
        # ページがサーバー上で見つかるかどうかをチェック。
        try:
            category_html = urlopen(url)

        except HTTPError as e:
            # エラーの内容を端末に出力
            print(e)
            continue
        # 各カテゴリーのhtmlオブジェクトを作成
        # サーバーがあるかどうかをチェック。
        try:
            category_object = BeautifulSoup(category_html.read())
        except URLError as e:
            # エラーの内容を端末に出力
            print(e)
            continue

        # 一つのカテゴリーページのページ番号をCATEGORY_STARTからCATEGORY_ENDまで取得。
        category_page_urls = ["%s?page=%s" % (url, category_page_index)
                              for category_page_index
                              in range(CATEGORY_START, CATEGORY_END + 1)]

        for category_page_url in category_page_urls:
            # 各カテゴリーのページurlのhtmlのタイトルとコンテンツを取得し、ナイーブベイズ分類器で学習させる。
            # try文でカプセル化します。
            # 各カテゴリーのhtmlを取得
            # ページがサーバー上で見つかるかどうかをチェック。
            try:
                category_page_html = urlopen(category_page_url)
            except HTTPError as e:
                # エラーの内容を端末に出力
                print(e)
                continue
                # 各カテゴリーのhtmlオブジェクトを作成
                # サーバーがあるかどうかをチェック。
            try:
                category_page_object = BeautifulSoup(category_page_html.read())
            except URLError as e:
                # エラーの内容を端末に出力
                print(e)
                continue

            for page_index in range(PAGE_TITLE_START, PAGE_TITLE_END):
                # csvを追記モードで開きます→ここでcsvを開くのはファイルが大きくなった時にcsvを開くのに時間がかかるためです

                try:
                    page_title = category_page_object.find_all("div", {"class": "list_title"})[
                        page_index].a.get_text()
                    article_text = category_page_object.find_all('div', {'class': "list_lead"})[
                        page_index].get_text()
                    #textdata = []
                    # textdata.append(article_text)
                    listdata = []
                    listdata.append(page_title)
                    listdata2 = []
                    listdata2.append(article_text)
                    #listdata3 = []
                    #listdata3.append("%s %s\n" % (listdata, " ".join(listdata2)))
                    # listdata3.append(%s %s % (page_title,article_text))
                    csvWriter.writerow(listdata + listdata2)
                    listd = []
                    listd.append(name)
                    csvWriter2.writerow(listd)
                    # if page_numbers % 100 == 0 :
                    #    listd = []
                    #    listd.append(name)
                    #    csvWriter2.writerow(listd)
                except AttributeError as e:
                    # エラーの内容を端末に出力
                    print(e)
                    continue
                    # 1行書き込み

                print("No%s,obj.train(%s,%s)" %
                      (page_numbers, page_title, name))
                #print ("%s" % article_text)
                page_numbers = page_numbers + 1
                # 取得したタイトルのテキストを学習させます。
                obj.train(page_title + article_text, name)
                # Gunosyのサイトでアクセス制限があれば以下の関数を利用して下さい。
                # time.sleep(1)
