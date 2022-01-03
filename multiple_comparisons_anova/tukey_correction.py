import pandas as pd
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd

np.random.seed(123)
a, b, c, d = [], [], [], []

df = pd.DataFrame({'RT': np.random.randn(100), 'Cond': np.random.choice(['A', 'B', 'C', 'D'], 100)})

for num, gr in df.Cond.items():
    match gr:
        case 'A':
            a.append(df.RT[num])
        case 'B':
            b.append(df.RT[num])
        case 'C':
            c.append(df.RT[num])
        case 'D':
            d.append(df.RT[num])

print(f'A: \n\tMean: {pd.Series(data=a).mean()}\n\tMedian: {pd.Series(data=a).median()}'
      f'\n\tMin: {min(pd.Series(data=a))}\n\tMax: {max(pd.Series(data=a))}\n'
      f'B: \n\tMean: {pd.Series(data=b).mean()}\n\tMedian: {pd.Series(data=b).median()}'
      f'\n\tMin: {min(pd.Series(data=b))}\n\tMax: {max(pd.Series(data=b))}\n'
      f'C: \n\tMean: {pd.Series(data=c).mean()}\n\tMedian: {pd.Series(data=c).median()}'
      f'\n\tMin: {min(pd.Series(data=c))}\n\tMax: {max(pd.Series(data=c))}\n'
      f'D: \n\tMean: {pd.Series(data=d).mean()}\n\tMedian: {pd.Series(data=d).median()}'
      f'\n\tMin: {min(pd.Series(data=d))}\n\tMax: {max(pd.Series(data=d))}\n')

hs_res = pairwise_tukeyhsd(df["RT"], df['Cond'])
print(hs_res)
