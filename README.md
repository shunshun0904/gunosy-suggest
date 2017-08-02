<<<<<<< HEAD
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
内のそれぞれの１から１００ページのタイトル。（カテゴリー内のページ数が１００までの表示なのでそのような仕様になっています。）


■訓練データとしてタイトルを選択した理由
１、タイトルはその記事の象徴しているから。
２、処理時間が短くなるから。

よって、訓練データ数は８(カテゴリー)×２０（カテゴリー１ページあたりの記事数）×100（ページ）=16000

また汎用性を持たせるためgettrain.pyモジュールの41行目と42行目のCATEGORY_PAGE_START_INDEX = 1、
CATEGORY_PAGE_END_INDEX = 100を変更すると取得するカテゴリーページを変更することが出来ます。

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


####その他の仕様
Gunosyのサイトをクローリングスクレイピングする際にアクセス制限がかかった場合はtime.sleepで時間間隔を
指定してアクセスをして下さい。
=======
# gunosy
>>>>>>> d625e8a84e05ef88f0d0556ed4a7c34726e646ae
