#
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import naivebayes


def gunosy_train(obj):

	#カテゴリーのurl
	gunosy_category_urls = [
	'https://gunosy.com/categories/1',  # エンタメ
	'https://gunosy.com/categories/2',  # スポーツ
	'https://gunosy.com/categories/3',  # おもしろ
	'https://gunosy.com/categories/4',  # 国内
	'https://gunosy.com/categories/5',  # 海外
	'https://gunosy.com/categories/6',  # コラム
	'https://gunosy.com/categories/7',  # IT・科学
	'https://gunosy.com/categories/8',  # グルメ
	]

	#カテゴリー名
	gunosy_category_names = [
	'エンタメ',
	'スポーツ',
	'おもしろ',
	'国内',
	'海外',
	'コラム',
	'IT・科学',
	'グルメ',
	]

	#各カテゴリー内のページ数(定数)
	CATEGORY_PAGE_START_NUMBER = 0
	CATEGORY_PAGE_END_NUMBER = 20


	for (category_url,category_name) in zip(gunosy_category_urls,gunosy_category_names):
		#try文でカプセル化します。
		#各カテゴリーのhtmlを取得
		#ページがサーバー上で見つかるかどうかをチェック。
		try:
			category_html = urlopen(category_url)
		except HTTPError as e:
			#エラーの内容を端末に出力
			print(e)
			continue
		#各カテゴリーのhtmlオブジェクトを作成
		#サーバーがあるかどうかをチェック。
		try:
			category_object = BeautifulSoup(category_html.read())
		except URLError as e:
			#エラーの内容を端末に出力
			print(e)
			continue

		#各カテゴリーのページurlのhtmlのタイトルとコンテンツを取得し、ナイーブベイズ分類器で学習させる。
		for page_number in range(CATEGORY_PAGE_START_NUMBER,CATEGORY_PAGE_END_NUMBER):

			try:
				page_title = category_object.find_all("div",{"class":"list_title"})[page_number].a.get_text()
			except AttributeError as e:
				#エラーの内容を端末に出力
				print(e)
				continue
			#デバックの確認です。
			print("obj.train(%s,%s)" %(page_title,category_name))
			#取得したタイトルのテキストを学習させます。
			obj.train(page_title,category_name)
			
			
			










