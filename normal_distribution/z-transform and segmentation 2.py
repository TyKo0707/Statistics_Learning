from scipy import stats
# "scipy.stats.norm.cdf()" is a cumulative (normal)distribution function
#  by known "z".
# How many % of the sample are less than a given value.
print(f'There are {stats.norm.cdf(0.8):.2%} values between [-∞ ; 0,8σ].')
# "scipy.stats.norm.sf()" - how many % of the sample are greater than a given value
print(f'There are {(stats.norm.sf(0.8)):.2%}  values between [0,8σ ; +∞].')
# "st.norm.cdf(z1) + st.norm.sf(z2)" - how many % of the sample
# are outside of the given interval.
print(f'There are {(stats.norm.sf(0.8) + stats.norm.cdf(-2)):.2%} values on the interval [-∞ ; -2σ]U[0,8σ ; +∞]')
# "st.norm.ppf" is inverse to "scipy.stats.norm.cdf()
print(f'st.norm.ppf(st.norm.cdf(0.8)) = {stats.norm.ppf(stats.norm.cdf(0.8)):.1f}')
print(f'st.norm.ppf(st.norm.cdf(-2)) = {stats.norm.ppf(stats.norm.cdf(-2)):.1f}')