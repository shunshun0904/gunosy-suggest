#coding:utf-8
import sys
from collections import defaultdict
from collections import Counter

# trans_data.py
# news20のデータセットをナイーブベイズで扱えるデータ形式に変換する
# http://people.csail.mit.edu/jrennie/20Newsgroups/
# 出力データフォーマット
# 1列目にカテゴリ、2列目以降は単語と出現頻度の組を列挙
# [category] [word:count] [word:count] ...  <- doc1
# [category] [word:count] [word:count] ...  <- doc2


def trans_data(categoryfile,datafile, outfile):
    # カテゴリをロード
    category = []
    fp = open("category.csv")  # test.mapでも同じ
    for line in fp:
        line = line.rstrip()
        category.append(line.split()[0])
    fp.close()

    # ストップワードをロード
    stopwords = []
    fp = open("stopwords.txt")
    for line in fp:
        line = line.rstrip()
        stopwords.append(line)
    fp.close()


    rownum = []
    fp = open("vocaburary.csv")
    for line in fp:
        line = line.strip()
        rownum.append(line.split()[0])
    # 総文書数
    num = len(rownum)

    # 変換
    train_data = []
    for i in range(num):
        train_data.append([])

    lineCount = 0
    fp = open("vocaburary.csv")
    for line in fp:
        lineCount += 1
        line = line.strip()
        itemList = line.split(',')
        counter = Counter(itemList)
        for word, cnt in counter.most_common():
            if not word in stopwords:  # ★ストップワードに登録されていない
                train_data[lineCount-1].append("%s:%d" % (word, cnt))
    fp.close()

    fp = open(outfile, "w")
    for i in range(num):
        fp.write("%s %s\n" % (category[i], " ".join(train_data[i])))
    fp.close()
    #    train_data.clear()

if __name__ == "__main__":
    # 訓練データを変換
    trans_data("category.csv", "vocaburary.csv" ,"gunosy-stop.csv")
    # テストデータを変換
    trans_data("category.csv", "vocaburary.csv" ,"gunosy-test-stop.csv")
