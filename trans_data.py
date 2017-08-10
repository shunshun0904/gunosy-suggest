# coding:utf-8
import sys
from collections import defaultdict
from collections import Counter

# trans_data.py
# スクレイピングしたデータをナイーブベイズで扱えるデータ形式に変換する
# 出力データフォーマット
# 1列目にカテゴリ、2列目以降は単語と出現頻度の組を列挙
# [category] [word:count] [word:count] ...  <- doc1
# [category] [word:count] [word:count] ...  <- doc2

# ストップワード込みのデータを作成する関数


def trans_data1(categoryfile, datafile, outfile):
    # カテゴリをロード
    category = []
    fp = open("category.csv")  # test.mapでも同じ
    for line in fp:
        line = line.rstrip()
        category.append(line.split()[0])
    fp.close()

    rownum = []
    fp = open("vocaburary.csv")
    for line in fp:
        line = line.strip()
        rownum.append(line.split()[0])
    # 総記事数
    num = len(rownum)

    # [word:count]の形式に変換したものを格納する配列の作成
    train_data = []
    for i in range(num):
        train_data.append([])

    # train_dataにデータを格納
    lineCount = 0
    fp = open("vocaburary.csv")
    for line in fp:
        lineCount += 1
        line = line.strip()
        itemList = line.split(',')
        counter = Counter(itemList)
        for word, cnt in counter.most_common():
            train_data[lineCount - 1].append("%s:%d" % (word, cnt))
    fp.close()

    fp = open(outfile, "w")
    for i in range(num):
        fp.write("%s %s\n" % (category[i], " ".join(train_data[i])))
    fp.close()


# ストップワードなしのデータを作成する関数
def trans_data2(categoryfile, datafile, outfile):
    # カテゴリをロード
    category = []
    fp = open("category.csv")  # test.mapでも同じ
    for line in fp:
        line = line.rstrip()
        category.append(line.split()[0])
    fp.close()

    rownum = []
    fp = open("vocaburary.csv")
    for line in fp:
        line = line.strip()
        rownum.append(line.split()[0])
    # 総記事数
    num = len(rownum)

    # [word:count]の形式に変換したものを格納する配列の作成
    train_data = []
    for i in range(num):
        train_data.append([])

    # ストップワードをロード
    stopwords = []
    fp = open("stopwords.txt")
    for line in fp:
        line = line.rstrip()
        stopwords.append(line)
    fp.close()

    # train_dataにデータを格納
    lineCount = 0
    fp = open("vocaburary.csv")
    for line in fp:
        lineCount += 1
        line = line.strip()
        itemList = line.split(',')
        counter = Counter(itemList)
        for word, cnt in counter.most_common():
            if word not in stopwords:  # ★ストップワードに登録されていない
                train_data[lineCount - 1].append("%s:%d" % (word, cnt))
    fp.close()

    fp = open(outfile, "w")
    for i in range(num):
        fp.write("%s %s\n" % (category[i], " ".join(train_data[i])))
    fp.close()


if __name__ == "__main__":
    # 訓練データを変換
    trans_data1("category.csv", "vocaburary.csv", "gunosy.csv")
    trans_data2("category.csv", "vocaburary.csv", "gunosy-stop.csv")
