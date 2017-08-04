import codecs
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import crossvalidation_stopword

print ("accuracy:", average)
height = np.array([ 0.7791,0.7690,0.6713,0.6256])
left = np.array([1,2,3,4])
label = ["Only_stopwords","Nothing","Chi-squared", "Mutual-info"]
plt.bar(left, height,tick_label=label, align="center")
for x, y in zip(left, height):
    plt.text(x, y, y, ha='center', va='bottom')

plt.ylabel("accuracy")
plt.title("Comparison of Stopwords")
plt.legend()
plt.ylim(ymax = 1.0, ymin = 0)
plt.show()
filename = "comparison_stopwords-hoge.png"
plt.savefig(filename)
