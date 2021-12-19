from scipy import stats
from numpy import sqrt

p = 0.95
# computing alpha-level
alpha = (1 - p) / 2
# isf - Inverse survival function (inverse of sf)
print(f'{stats.norm().isf(alpha):.2f} sigma')  # 1.96 sigma

"""
Exercise:
Calculate the 99% confidence interval for the following example:
mean = 10, standard deviation = 5, sample size = 100
"""

p = 0.99
mean = 10
std = 5
n = 100

se = std / sqrt(n)
alpha = (1 - p) / 2
sigma = stats.norm().isf(alpha)
conf_interv = mean - sigma * se, mean + sigma * se
print('[%.2f; %.2f]' % conf_interv)
