import pandas as pd
from scipy.stats import t
import matplotlib.pyplot as plt
import numpy as np

array1 = np.array([84.7, 105.0, 98.9, 97.9, 108.7, 81.3, 99.4, 89.4, 93.0,
                   119.3, 99.2, 99.4, 97.1, 112.4, 99.8, 94.7, 114.0, 95.1, 115.5, 111.5])
array2 = np.array([57.2, 68.6, 104.4, 95.1, 89.9, 70.8, 83.5, 60.1, 75.7,
                   102.0, 69.0, 79.6, 68.9, 98.6, 76.0, 74.8, 56.0, 55.6, 69.4, 59.5])

# count amount of elements, mean, standard deviation and standard error of mean
df = pd.DataFrame({'Sample1': array1, 'Sample2': array2}).agg(['mean', 'std', 'count', 'sem']).transpose()
df.columns = ['Mx', 'SD', 'N', 'SE']

# calculate the 95% deviation interval of the mean
p = 0.95
K = t.ppf((1 + p) / 2, df['Mx'] - 1)
df['interval'] = K * df['SE']
print(df)

# build plots, boxplot using begin elements of array1, array2, confidence intervals from dataframe df
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 9))

# boxplot
bplot1 = ax1.boxplot([array1, array2],
                     vert=True,  # creating vertical boxes
                     patch_artist=True,  # use colors for quantiles boxes
                     labels=['Sample1', 'Sample2'])

# confidence intervals plot
bplot2 = ax2.errorbar(x=df.index, y=df['Mx'], yerr=df['interval'], color="black", capsize=3,
                      mfc="red", mec="black", fmt='o')

# paint boxplot
colors = ['pink', 'lightgreen']
for patch, color in zip(bplot1['boxes'], colors):
    patch.set_facecolor(color)

# add common data for each plot
for ax in [ax1, ax2]:
    ax.yaxis.grid(True)
    ax.set_title('Melting temperature of two types of DNA ')
    ax.set_xlabel('Comparison of two samples ')
    ax.set_ylabel('Temperature F')

plt.show()
