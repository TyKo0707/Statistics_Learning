"""
It is believed that the IQ value (level of intelligence) in humans has a normal distribution.
with a mean of 100 and a standard deviation of 15 (M = 100, sd = 15).
What percentage of people have an IQ> 125?
"""

from scipy import stats

mean = 100
std = 15
IQ = 125
# sf - Survival function = (1 - cdf) - Cumulative distribution function
print(
    f"Only {(stats.norm(mean, std).sf(IQ)) * 100:.2f}% of all people have IQ more than {IQ}")  # Only 4.78% of all people have IQ more than 125
