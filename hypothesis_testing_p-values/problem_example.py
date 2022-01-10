"""
A neurologist is testing the effect of a drug on response time by injecting
100 rats with a unit dose of the drug, subjecting each to neurological stimulus, and
recording its response time. The neurologist knows that the mean response time for rats
not injected with the drug is 1.2 seconds. The mean of the 100 injected rats' response
times is 1.05 seconds with a sample standard deviation of 0.5 seconds.
Do you think that the drug has an effect on response time?
"""

from scipy import stats
from math import sqrt

n = 100
mean = 1.2
mean_sample = 1.05
std = 0.5
threshold = 0.01
se = std / sqrt(n)
p = 2 * stats.norm(mean, se).cdf(mean_sample)

if p < threshold:
    print(f'Null hypothesis can be rejected since p \u2248 {p:.3f} < {threshold}\n'
          f'This means that the drug most likely has an effect on response time.')
else:
    print(f'Null hypothesis cannot be rejected since p \u2248 {p:.3f} <= {threshold}\n'
          f'This means that the drug unlikely has an effect on response time.')