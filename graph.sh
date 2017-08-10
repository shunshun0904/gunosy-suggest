# ４パターンの交差検定による精度検証を実施
#　hoge.csvに精度を出力する

python crossvalidation_stopword_normal.py
echo $(python crossvalidation_stopword_normal.py) > hoge.csv
python crossvalidation_normal.py
echo $(python crossvalidation_normal.py) >> hoge.csv
python crossvalidation_stopword_Chi2.py
echo $(python crossvalidation_stopword_Chi2.py) >> hoge.csv
python crossvalidation_stopword_Mutual.py
echo $(python crossvalidation_stopword_Mutual.py) >> hoge.csv
