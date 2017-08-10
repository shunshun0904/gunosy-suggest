# ４パターンの精度を比較するグラフの作成をするスクリプト
# graph.sh を先に動かし、4パターンの計算を先に行わないとグラフはできない
import codecs
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#4パターンの精度を配列に格納
height = []
fp = open("hoge.csv")
for line in fp:
    line = line.rstrip()
    height.append(line.split()[0])
fp.close()

#棒グラフの作成
left = np.array([1, 2, 3, 4])
label = ["Only_stopwords", "Nothing", "Chi-squared", "Mutual-info"]
plt.bar(left, height, tick_label=label, align="center")
for x, y in zip(left, height):
    plt.text(x, y, y, ha='center', va='bottom')

plt.ylabel("accuracy")
plt.title("Comparison of Stopwords")
plt.legend()
plt.ylim(ymax=1.0, ymin=0)
plt.show()
filename = "comparison_stopwords.png"
plt.savefig(filename)
