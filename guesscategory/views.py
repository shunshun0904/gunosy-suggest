from django.http.response import HttpResponse
from django.shortcuts import render # 追加する
from datetime import datetime #追加する
import naivebayes
import inputscraping
import scraiping


#Gunosyのサイトをスクレイピングをします。
nb = naivebayes.NaiveBayes()
#Gunosyのサイトの記事データを用いて訓練させます。
scraiping.gunosy_train(nb)



def hello_guess_category(request):

	url = request.GET.get('url')

	#urlが入力されると
	if url != None and url !='':
		urltext = inputscraping.url_to_text(url)
		category = "推定カテゴリー ：" + nb.classifier(urltext)
	#urlが入力していないときの処理。
	else:
		category = "urlを入力して下さい。"


	d = {
	    'category': category
	}
	return render(request, 'index.html', d)






