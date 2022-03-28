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
