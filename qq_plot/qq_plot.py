import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [12, 6]

mu, sigma = 10, 4
n = 1000
sequence = np.random.normal(mu, sigma, n)

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('QQ Plot', fontsize=18)

# Q-Q Plot graph
stats.probplot(sequence, dist="norm", plot=ax1)
ax1.set_title("Normal Q-Q Plot")

# normal distribution histogram + distribution
count, bins, _ = ax2.hist(sequence, 25, density=True)
p_x = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2))
ax2.plot(bins, p_x, color='r')

plt.show()
