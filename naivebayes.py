# -*- coding: utf-8 -*-
import math
import sys

# yahoo!形態素解析
import morphological


def getwords(doc):
    words = [s.lower() for s in morphological.split(doc)]
    return tuple(w for w in words)


class NaiveBayes:

    def __init__(self):
        self.vocabularies = set()  # 単語の集合
        self.wordcount = {}       # {category : { words : n, ...}}
        self.catcount = {}        # {category : n}

    def wordcountup(self, word, cat):
        self.wordcount.setdefault(cat, {})
        self.wordcount[cat].setdefault(word, 0)
        self.wordcount[cat][word] += 1
        self.vocabularies.add(word)

    def catcountup(self, cat):
        self.catcount.setdefault(cat, 0)
        self.catcount[cat] += 1

    def train(self, doc, cat):
        word = getwords(doc)
        for w in word:
            self.wordcountup(w, cat)
        self.catcountup(cat)

    def classifier(self, doc):
        best = None  # 最適なカテゴリ
        max = -sys.maxsize
        word = getwords(doc)

        # カテゴリ毎に確率の対数を求める
        for cat in list(self.catcount.keys()):
            prob = self.score(word, cat)
            if prob > max:
                max = prob
                best = cat

        return best

    def score(self, word, cat):
        score = math.log(self.priorprob(cat))
        for w in word:
            score += math.log(self.wordprob(w, cat))
        return score

    def priorprob(self, cat):
        return float(self.catcount[cat]) / sum(self.catcount.values())

    def incategory(self, word, cat):
        # あるカテゴリの中に単語が登場した回数を返す
        if word in self.wordcount[cat]:
            return float(self.wordcount[cat][word])
        return 0.0

    def wordprob(self, word, cat):
        # P(word|cat)が生起する確率を求める
        prob = \
            (self.incategory(word, cat) + 1.0) / \
            (sum(self.wordcount[cat].values()) +
             len(self.vocabularies) * 1.0)
        return prob
