# coding:utf-8
# カイ２乗値による特徴選択を行うプログラム
import codecs
import math
import sys
from collections import defaultdict

# feature_selection.py


def chisquare(target, data, k=0):
    """カテゴリtargetにおけるカイ二乗値が高い上位k件の単語を返す"""
    # 上位k件を指定しないときはすべて返す
    if k == 0:
        k = sys.maxsize

    V = set()
    N11 = defaultdict(float)  # N11[word] -> wordを含むtargetの文書数
    N10 = defaultdict(float)  # N10[word] -> wordを含むtarget以外の文書数
    N01 = defaultdict(float)  # N01[word] -> wordを含まないtargetの文書数
    N00 = defaultdict(float)  # N00[word] -> wordを含まないtarget以外の文書数
    Np = 0.0  # targetの文書数
    Nn = 0.0  # target以外の文書す

    # N11とN10をカウント
    for d in data:
        cat, words = d[0], d[1:]
        if cat == target:
            Np += 1
            for wc in words:
                word, count = wc.split(":")
                V.add(word)
                N11[word] += 1  # 文書数をカウントするので+1すればOK
        elif cat != target:
            Nn += 1
            for wc in words:
                word, count = wc.split(":")
                V.add(word)
                N10[word] += 1

    # N01とN00は簡単に求められる
    for word in V:
        N01[word] = Np - N11[word]
        N00[word] = Nn - N10[word]
    # 総文書数
    N = Np + Nn

    # 各単語のカイ二乗値を計算
    chiSquare = []
    for word in V:
        n11, n10, n01, n00 = N11[word], N10[word], N01[word], N00[word]

        # カテゴリと単語が独立である（帰無仮説）と仮定したときの期待値を求める
        e11 = (n10 + n11) * (n01 + n11) / float(N)
        e10 = (n10 + n11) * (n00 + n10) / float(N)
        e01 = (n00 + n01) * (n01 + n11) / float(N)
        e00 = (n00 + n01) * (n00 + n10) / float(N)

        # カイ二乗値の各項を計算
        score = (n00 - e00)**2 / e00 + (n01 - e01)**2 / e01 + \
            (n10 - e10)**2 / e10 + (n11 - e11)**2 / e11
        chiSquare.append((score, word))

    # カイ二乗値の降順にソートして上位k個を返す
    chiSquare.sort(reverse=True)
    return chiSquare[0:k]


if __name__ == "__main__":
    # 訓練データをロード
    trainData = []
    fp = codecs.open("gunosy.csv", "r", "utf-8")
    for line in fp:
        line = line.rstrip()
        temp = line.split()
        trainData.append(temp)
    fp.close()

    # カイ二乗値を用いて特徴選択
    target = "海外"
    features = chisquare(target, trainData, k=5)
    print("[%s]" % target)
    for score, word in features:
        print(score, word)
