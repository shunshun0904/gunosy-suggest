# coding:utf-8
# 相互情報量による特徴選択を行うプログラム
import codecs
import math
import sys
from collections import defaultdict

# feature_selection.py


def mutual_information(target, data, k=0):
    """カテゴリtargetにおける相互情報量が高い上位k件の単語を返す"""
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

    # 各単語の相互情報量を計算
    MI = []
    for word in V:
        n11, n10, n01, n00 = N11[word], N10[word], N01[word], N00[word]
        # いずれかの出現頻度が0.0となる単語はlog2(0)となってしまうのでスコア0とする
        if n11 == 0.0 or n10 == 0.0 or n01 == 0.0 or n00 == 0.0:
            MI.append((0.0, word))
            continue
        # 相互情報量の定義の各項を計算
        temp1 = n11 / N * math.log((N * n11) / ((n10 + n11) * (n01 + n11)), 2)
        temp2 = n01 / N * math.log((N * n01) / ((n00 + n01) * (n01 + n11)), 2)
        temp3 = n10 / N * math.log((N * n10) / ((n10 + n11) * (n00 + n10)), 2)
        temp4 = n00 / N * math.log((N * n00) / ((n00 + n01) * (n00 + n10)), 2)
        score = temp1 + temp2 + temp3 + temp4
        MI.append((score, word))

    # 相互情報量の降順にソートして上位k個を返す
    MI.sort(reverse=True)
    return MI[0:k]


if __name__ == "__main__":
    # 訓練データをロード
    trainData = []
    fp = codecs.open("gunosy.csv", "r", "utf-8")
    for line in fp:
        line = line.rstrip()
        temp = line.split()
        trainData.append(temp)
    fp.close()
    # 相互情報量を用いて特徴選択
    target = "海外"
    features = mutual_information(target, trainData, k=5)
    print("[%s]" % target)
    for score, word in features:
        print(score, word)
