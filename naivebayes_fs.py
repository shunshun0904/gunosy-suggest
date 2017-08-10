# coding:utf-8
# 特徴選択（相互情報量による）を行うナイーブベイズ分類器（精度検証用）
import math
import sys
from collections import defaultdict
from feature_selection import mutual_information


class NaiveBayes:
    """Multinomial Naive Bayes"""

    def __init__(self, k):
        self.categories = set()     # カテゴリの集合
        self.vocabularies = set()   # ボキャブラリの集合
        self.wordcount = {}         # wordcount[cat][word] カテゴリでの単語の出現回数
        self.catcount = {}          # catcount[cat] カテゴリの出現回数
        self.denominator = {}       # denominator[cat] P(word|cat)の分母の値
        self.k = k                  # ボキャブラリ数

    def train(self, data):
        """ナイーブベイズ分類器の訓練"""
        # 文書集合からカテゴリを抽出して辞書を初期化
        for d in data:
            cat = d[0]
            self.categories.add(cat)
        for cat in self.categories:
            self.wordcount[cat] = defaultdict(int)
            self.catcount[cat] = 0

        # 特徴選択してボキャブラリを絞り込む
        L = []
        for cat in self.categories:
            features = mutual_information(cat, data)
            L.extend(features)
        L.sort(reverse=True)
        for i in range(len(L)):
            # L[i]=(score, word)なので単語はL[i][1]で取り出せる
            self.vocabularies.add(L[i][1])
            # ボキャブラリの数が指定した数に達したら終了
            if len(self.vocabularies) == self.k:
                break

        # 文書集合からカテゴリと単語をカウント
        for d in data:
            cat, doc = d[0], d[1:]
            self.catcount[cat] += 1
            for wc in doc:
                word, count = wc.split(":")
                count = int(count)
                # 単語がボキャブラリに含まれなければ無視
                if word not in self.vocabularies:
                    continue
                self.wordcount[cat][word] += count
        # 単語の条件付き確率の分母の値をあらかじめ一括計算しておく（高速化のため）
        for cat in self.categories:
            self.denominator[cat] = sum(
                self.wordcount[cat].values()) + len(self.vocabularies)

    def classify(self, doc):
        """事後確率の対数 log(P(cat|doc)) がもっとも大きなカテゴリを返す"""
        best = None
        max = -sys.maxsize

        for cat in self.catcount.keys():
            p = self.score(doc, cat)
            if p > max:
                max = p
                best = cat
        return best

    def wordProb(self, word, cat):
        """単語の条件付き確率 P(word|cat) を求める"""
        # ラプラススムージングを適用
        # 分母はtrain()の最後で一括計算済み
        return float(self.wordcount[cat][word] + 1) / \
            float(self.denominator[cat])

    def score(self, doc, cat):
        """文書が与えられたときのカテゴリの事後確率の対数 log(P(cat|doc)) を求める"""
        total = sum(self.catcount.values())  # 総文書数
        score = math.log(float(self.catcount[cat]) / total)  # log P(cat)
        for wc in doc:
            word, count = wc.split(":")
            count = int(count)
            # 単語がボキャブラリに含まれなければ無視
            if word not in self.vocabularies:
                continue
            # logをとるとかけ算は足し算になる
            for i in range(count):
                score += math.log(self.wordProb(word, cat))  # log P(word|cat)
        return score

    def __str__(self):
        total = sum(self.catcount.values())  # 総文書数
        return "documents: %d, vocabularies: %d, categories: %d" % (
            total, len(self.vocabularies), len(self.categories))
