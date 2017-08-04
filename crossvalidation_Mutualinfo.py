# coding:utf-8
import codecs
import sys
import matplotlib
import matplotlib.pyplot as plt
from naivebayes_fs import NaiveBayes  # 特徴選択（相互情報量）付きのナイーブベイズを使う
matplotlib.use('Agg')

klist2 = []
aclist2 = []
for i in range(4000, 8000, 2000):  # 特徴語数（1801まで）、数パターン（200語おきに）計算
    K = i
    klist2.append(K)
    number = []
    fp = open("gunosy.csv")  # test.mapでも同じ
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
            #print (nb)
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
        #print (accuracyList)
        average = sum(accuracyList) / float(N)
        aclist2.append(average)
        return average

    if __name__ == "__main__":
        # ブログデータをロード
        data = []
        fp = codecs.open("gunosy.csv", "r", "utf-8")
        for line in fp:
            line = line.rstrip()
            temp = line.split()
            data.append(temp)
        fp.close()
        # N-fold Cross Validationで分類精度を評価
        average = crossValidation(data, N=num, randomize=True)

        print("accuracy:", average)

        fig = plt.figure()
        ax = plt.gca()
        #ax.plot(klist,aclist, c='b', label="nothing")
        #ax.plot(klist1,aclist1, c='r', label="Mutual information")
        ax.plot(klist2, aclist2, "-o", c='b', label="Mutual information")
        ax.set_xlabel("vocaburary size ")
        ax.set_ylabel("accuracy")
        ax.set_title("acucuracy-vocabulalysize")
        plt.legend()
        plt.xlim(0, 8100)
        plt.ylim(0, 1.0)
        plt.show()
        filename = "feature_selection_mutual-hoge.png"
        plt.savefig(filename)
