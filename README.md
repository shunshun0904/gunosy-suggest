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

