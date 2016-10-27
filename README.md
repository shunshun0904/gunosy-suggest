##制作物
記事URLを入れると記事カテゴリを返す、ナイーブベイズを使った教師あり文書分類器ウェブアプリの実装

####開発環境
```
Python 3.5
Django 1.10
```

####訓練データ
```
GunosyのWebサイト(https://gunosy.com/)のエンタメ,スポーツ,おもしろ,国内,海外,コラム,IT・科学,グルメカテゴリー
内のそれぞれの1ページ目の２０記事のタイトルのみ(8×20記事=160記事)  
```

####実行方法

１、課題のgunosyフォルダをクローン  
```
$git clone https://github.com/shotanaka0513/gunosy.git  
```
２、クローンしたgunosyフォルダへ移動  
```
$cd gunosy    
```
３、lsコマンドでgunosyフォルダ内を確認  
```
$ls 
  
README.md		gunosy			naivebayes.py
__pycache__		inputscraping.py	scraiping.py
db.sqlite3		manage.py		templates
guesscategory		morphological.py
```

４、現在いるフォルダが３のようになったら以下のコマンドでサーバーを起動  
```
$python manage.py runserver　　
```

５、サーバーを起動後gunosyサイトの記事を訓練させているため、少し（３０秒ぐらい）待ちます。  

６、５を終了後、ブラウザに以下のurlにアクセス  
http://127.0.0.1:8000/guesscategory/

７、フォームに記事urlを入力  

８、訓練データを元に入力された記事urlのカテゴリが返ってくる。
