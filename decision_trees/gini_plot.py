from __future__ import print_function, division
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

plt.rcParams['figure.figsize'] = (6, 4)
xx = np.linspace(0, 1, 50)
plt.plot(xx, [2 * x * (1 - x) for x in xx], label='gini')
plt.plot(xx, [4 * x * (1 - x) for x in xx], label='2*gini')
plt.plot(xx, [-x * np.log2(x) - (1 - x) * np.log2(1 - x) for x in xx], label='entropy')
plt.plot(xx, [1 - max(x, 1 - x) for x in xx], label='missclass')
plt.plot(xx, [2 - 2 * max(x, 1 - x) for x in xx], label='2*missclass')
plt.xlabel('p+')
plt.ylabel('criterion')
plt.title('Quality criteria as p+ functions (binary classification)')
plt.legend()
plt.show()

# first class
np.random.seed(7)
train_data = np.random.normal(size=(100, 2))
train_labels = np.zeros(100)

# second class
train_data = np.r_[train_data, np.random.normal(size=(100, 2), loc=2)]
train_labels = np.r_[train_labels, np.ones(100)]

plt.rcParams['figure.figsize'] = (10, 8)
x = train_data[:, 0]
y = train_data[:, 1]
plt.scatter(x, y, c=train_labels, s=100,
            cmap='autumn', edgecolors='black', linewidth=1.5)
plt.plot(range(-2, 5), range(4, -3, -1))
plt.show()

