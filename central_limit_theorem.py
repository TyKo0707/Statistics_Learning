import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# values
dice = [1, 2, 3, 4, 5, 6]

# number of dice rolls
count = 6

# Statistical population size
sp_size = 10000

# sp - Statistical population - генеральная совокупность
sp = pd.Series(dtype=np.int64, index=range(sp_size))

for i in range(sp_size):
    value = 0
    for _ in range(count):
        value += np.random.choice(dice)
    sp[i] = value

sp.plot.hist(bins=28)

# number of samples
samples_count = 10

# size of each sample
sample_size = 200

samples = pd.DataFrame([[np.random.choice(sp) for _ in range(sample_size)] for __ in range(samples_count)]).T

means = samples.mean()
print('Comparing average of statistical population and average of each sample', sp.mean(),
      means.mean())  # Comparing average of statistical population and average of each sample 20.9756 20.881
print('Difference:', round(abs(means.mean() - sp.mean()), 3), ', standard error: ',
      round(means.std(), 3))  # Difference: 0.042 , standard error:  0.424

# lets take random sample
sample = samples[0]
print('Sample mean:', sample.mean())  # Sample mean: 20.755
print('Sample SE: ', round((sample.std() / math.sqrt(sample.size)), 3))  # Sample SE:  0.304

samples.hist(figsize=(16, 10), sharex=0)
plt.subplots_adjust(hspace=0.6)
plt.show()
