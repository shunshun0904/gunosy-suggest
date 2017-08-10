
##制作物
```
:記事URLを入れると記事カテゴリを返す、ナイーブベイズを使った教師あり文書分類器ウェブアプリの実装
:分類精度の確認及び、精度向上のための手法比較の結果
```
####開発環境
```
Python 3.6
Django 1.11.3
```
####コード規約
```
travis-ciを使うことで自動でPEP8のチェックができる
```
####訓練データ
```
GunosyのWebサイト(https://gunosy.com/)のエンタメ,スポーツ,おもしろ,国内,海外,コラム,IT・科学,グルメカテゴリー
800記事（100記事×8カテゴリー）のタイトル及び、リード文を学習データとして用いる。


■訓練データとしてタイトルとリード文を選択した理由
１、タイトルはその記事の象徴しているから。
２、タイトルのみでは単語数が少なく精度が悪かったため、リード文も用いた。（なお今回は精度向上の解決策にはそれを含めていない）


よって、訓練データ数は８(カテゴリー)×２０（カテゴリー１ページあたりの記事数）×（ページ）=800

また汎用性を持たせるためgettrain.pyモジュールの30行目と31行目のCATEGORY_PAGE_START_INDEX = 1、
CATEGORY_PAGE_END_INDEX = 100を変更すると取得するカテゴリーページを変更することが出来る。

■形態素解析について
今回、形態素解析をするにあたり用いた品詞は（名詞、動詞、形容詞、形容動詞）である。
```

####実行方法
```
１、課題のgunosyフォルダをクローン  

$git clone https://github.com/shotanaka0513/gunosy.git  

２、クローンしたgunosyフォルダへ移動  

$cd gunosy    

３、lsコマンドでgunosyフォルダ内を確認  

$ls

README.md                         crossvalidation_stopword_Mutual.py  gethtmltext.py   manage.py             requirements.txt
__pycache__                       crossvalidation_stopword_normal.py  gettrain.py      morphological.py      setup.py
category.csv                      db.sqlite3                          graph.sh         naivebayes.py         stopwords.txt
comparison_stopwords.png          feature_selection.py                guesscategory    naivebayes_fs.py      subject.csv
crossvalidation_Chi2.py           feature_selection_all.py            gunosy           naivebayes_fskai2.py  tasks.py
crossvalidation_Mutualinfo.py     feature_selection_ka2.png           gunosy-stop.csv  naivebayes_normal.py  templates
crossvalidation_normal.py         feature_selection_mutual.png        gunosy.csv       pip.txt               trans_data.py
crossvalidation_stopword_Chi2.py  feature_selectionkai2.py            hoge.csv         requirements-dev.txt  vocaburary.csv


４、現在いるフォルダが３のようになったら以下のコマンドでサーバーを起動  

$python manage.py runserver　0:8000　


５、サーバーを起動後gunosyサイトの記事を訓練させているため、少し（３０秒ぐらい）待ちます。  

６、５を終了後、ブラウザに以下のurlにアクセス  
http://127.0.0.1:8000/guesscategory/

７、フォームに記事urlを入力  

８、訓練データを元に入力された記事urlのカテゴリが返ってくる。

```

####精度の確認方法
```
■精度検証について
精度検証にはデータ数が少ないこともあり、「交差検定（leave one out）」を用いた。

１、python trans_data.pyを実行
取得したデータを[カテゴリー　単語：単語数]のようにデータ形式を変換する。（gunosy.csvが作成される）

２、python crossvalidation_normal.py を実行
交差検定をし、精度を評価する。
分類精度は0.7835　である。
```


####分類性能の向上と精度の比較
```
■精度向上の手法
ストップワードと２種類の特徴選択（相互情報量、カイ２乗値）を用いる手法を組み合わせて、分類性能の比較をした。

■ストップワードについて
stopwords.txtにまとめてある。（参考にしたサイトhttp://qiita.com/HirofumiYashima/items/e588ea80deac090bc4b3）

以下に、（1）ナイーブベイズとストップワード、(2）ナイーブベイズのみ、（3）ナイーブベイズとストップワード、カイ２乗値による抽出,
（4）ナイーブベイズとストップワード、相互情報量による抽出、
の４パターンでの精度を示す。なお特徴選択に用いた単語数は５００とした（除去する単語数に限らず、精度は悪くなる。詳細は後述する。）。

```

<img src="https://user-images.githubusercontent.com/25298659/28904628-4fb2bc98-7847-11e7-8260-86d79efdf83c.png"  title="サンプル" >

以上より、特徴選択は行わずに、ストップワードの除去のみ用いたほうが精度が若干向上することがわかる。


■上記グラフの作成手順

１、以下のコマンドで、4パターンについて計算を実行し、精度をhoge.csvに保存する

$sh graph.sh

２、以下のコマンドを実行し、hoge.csvを用いてグラフの作成  (comparison_stopwords.png)

$python feature_selection_all.py

■特徴選択による精度の確認
一般的には特徴選択を用いた単語の除去は精度が向上するが、今回は相互情報量、カイ２乗値による特徴選択を用いると精度が悪化した。
以下に選択単語数が1〜1800までの時の精度のグラフを示す。単語数が多くなるにつれ、特徴選択を用いなかった分類器の精度に近くなる。
```

<img src="https://user-images.githubusercontent.com/25298659/28902353-550d955e-7839-11e7-942d-18e0a14a46a6.png"  title="相互情報量による特徴選択" >　<img src="https://user-images.githubusercontent.com/25298659/28902363-682f2c56-7839-11e7-9b2f-fcab9a3f19f8.png"  title="カイ２乗値による特徴選択" >　

■上記グラフの作成手順
