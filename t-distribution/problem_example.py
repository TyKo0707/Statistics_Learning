"""
The mean emission of all engines of a new design needs to be below 20 ppm
if the design is to meet new emission requirements. Ten engines are
manufactured for testing purposes, and the emission level of each is determined.
The emission data is:
15.6 16.2 22.5 20.5 16.4 19.4 16.6 17.9 12.7 13.9
Does the data supply sufficient evidence to conclude that this type of engine
meets the new standard? Assume we are willing to risk a Type 1 error
with probability = 0.01
"""

from scipy import stats
import numpy as np
from math import sqrt

data = np.array([15.6, 16.2, 22.5, 20.5, 16.4, 19.4, 16.6, 17.9, 12.7, 13.9])
n = 10
df = n - 1  # degrees of freedom
mean = 20
threshold = 0.01  # the probability level below which H_0 can be rejected
sample_mean = data.mean()
std = np.std(data, ddof=1)
t = (sample_mean - mean) / (std / sqrt(n))
p = stats.t.cdf(t, df)

if p < threshold:
    print(f'The null hypothesis can be rejected since p = {p} < {threshold}.\n'
          f'There is a lower than 1% chance of making a Type 1 error.\n'
          f'This type of engine most likely meets the new standard')
else:
    print(f'The null hypothesis cannot be rejected since p = {p} >= {threshold}.')

