import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = dict()
# HAMILTON DESK
N = 10000  # Number of balls
level = 20  # Number of levels
for _ in range(N):
    index = 0
    for _ in range(level):
        index += np.random.choice([-1, 1])
    data.setdefault(index, 0)
    data[index] += 1

sns.set_theme(style="whitegrid")
sns.barplot(x=list(data.keys()), y=list(data.values()))
plt.show()
