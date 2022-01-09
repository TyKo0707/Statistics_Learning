"""We're trying to test whether a new low-fat diet actually helps obese people lose weight.
100 randomly assigned obese people are assigned to group 1 and put on the low fat diet.
Another 100 randomly assigned obese people are assigned to group 2 and put on a diet of
approximately the same amount of food, but not as low in fat. After 4 months, the mean
weight loss was 9.31 lbs. for group 1 (s=4.67) and 7.40 lbs. (s=4.04) for group 2.
"""

from scipy import stats
from math import sqrt

n = 100
mean_1 = 9.31
std_1 = 4.67
mean_2 = 7.40
std_2 = 4.04
p = 0.95
alpha = (1-p)/2

mean_difference = mean_1 - mean_2
se_difference = sqrt(std_1 ** 2 / n + std_2 ** 2 / n)  # since n > 30,
# we can use the stds of the samples
sigma = stats.norm().isf(alpha)
confidence_interval = mean_difference - sigma * se_difference, mean_difference + sigma * se_difference

confidence_interval_str = '[%.2f; %.2f]' % confidence_interval
print(f"""There is a 95% chance that the mean of statistical population lies within {confidence_interval_str}, so 
it's greater than zero. This means that a new low-fat diet is most likely more effective.""")