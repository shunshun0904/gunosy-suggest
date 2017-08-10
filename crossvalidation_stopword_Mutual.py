# coding:utf-8
# ストップワード除去あり、相互情報量による抽出ありの交差検定プログラム
import codecs
import sys
import matplotlib
import matplotlib.pyplot as plt
from naivebayes_fs import NaiveBayes  # 特徴選択（相互情報量）付きのナイーブベイズを使う
matplotlib.use('Agg')
# 特徴語抽出数
K = 500


number = []
fp = open("gunosy-stop.csv")  # test.mapでも同じ
for line in fp:
    line = line.rstrip()
    number.append(line.split()[0])
fp.close()

num = len(number)


def crossValidation(data, N=num, randomize=False):
    """N-fold Cross Validationで分類精度を評価"""
    # データをシャッフル
    if randomize:
        from random import shuffle
        shuffle(data)

    # N-fold Cross Validationで分類精度を評価
    accuracyList = []
    for n in range(N):  # 各分割について
        # 訓練データとテストデータにわける
        trainData = [d for i, d in enumerate(data) if i % N != n]
        testData = [d for i, d in enumerate(data) if i % N == n]
        # ナイーブベイズ分類器を学習
        nb = NaiveBayes(K)
        nb.train(trainData)
        # テストデータの分類精度を計算
        hit = 0
        numTest = 0
        for d in testData:
            correct = d[0]
            words = d[1:]
            predict = nb.classify(words)
            if correct == predict:
                hit += 1
            numTest += 1
        accuracy = float(hit) / float(numTest)
        accuracyList.append(accuracy)
    # N回の平均精度を求める
    average = sum(accuracyList) / float(N)
    average_f = round(average, 4)
    return average


if __name__ == "__main__":
    # ブログデータをロード
    data = []
    fp = codecs.open("gunosy-stop.csv", "r", "utf-8")
    for line in fp:
        line = line.rstrip()
        temp = line.split()
        data.append(temp)
    fp.close()
    # N-fold Cross Validationで分類精度を評価
    average = crossValidation(data, N=num, randomize=True)
    average_f = round(average, 4)
    print(average_f)
