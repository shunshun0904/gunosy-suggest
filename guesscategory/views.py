#命名規則： PEP8
from django.http.response import HttpResponse
from django.shortcuts import render # 追加する
from datetime import datetime #追加する
import naivebayes
import gethtmltext
import gettrain


#Gunosyのサイトをスクレイピングをします。
nb = naivebayes.NaiveBayes()
#Gunosyのサイトの記事データを用いて訓練させます。
gettrain.gunosy_train(nb)
# nb.train("ラーメン","食べ物")


def hello_guess_category(request):

	#フォームからurlを取得
	url = request.GET.get('url')
	#urlのhtmlファイルのテキストを取得
	html_text = gethtmltext.url_to_text(url)
	#エラーが出た場合の処理
	if html_text == None:
		category = "urlを入力して下さい。"
	#エラが無かった場合の処理
	else:
		category = "推定カテゴリー ：" + nb.classifier(html_text)

	d = {
	    'category': category
	}
	return render(request, 'index.html', d)






