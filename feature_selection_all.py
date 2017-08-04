import codecs
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


height = np.array([0.7791878172588832, 0.7690355329949239,
                   0.6713197969543148, 0.6256345177664975])
left = np.array([1, 2, 3, 4])
label = ["Only_stopwords", "Nothing", "Chi-squared", "Mutual-info"]
plt.bar(left, height, tick_label=label, align="center")
for x, y in zip(X, elapsed):
    plt.text(x, y, y, ha='center', va='bottom')

plt.ylabel("accuracy")
plt.title("Comparison of Stopwords")
plt.legend()
plt.ylim(ymax=1.0, ymin=0)
plt.show()
filename = "comparison_stopwords.png"
plt.savefig(filename)
