import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

sample_np = np.array([185, 175, 170, 169, 171, 175, 157, 172, 170, 172, 167, 173, 168, 167, 166,
                      167, 169, 172, 177, 178, 165, 161, 179, 159, 164, 178, 172, 170, 173, 171])

sample_pd = pd.Series([185, 175, 170, 169, 171, 175, 157, 172, 170, 172, 167, 173, 168, 167, 166,
                       167, 169, 172, 177, 178, 165, 161, 179, 159, 164, 178, 172, 170, 173, 171])

# RANGE OF SAMPLE (SELECTION)

scope = np.ptp(sample_np)
print(f'The range of our sample array is {scope}')

# VARIANCE AND STANDARD DEVIATION NUMPY

variance_np = np.var(sample_np)
standard_dev_np = np.std(sample_np, ddof=1)

print(f'Standard deviation of array is {round(float(standard_dev_np), 3)} '
      f'with variance {round(float(variance_np), 3)}')  # Standard deviation of array is 6.003 with variance 34.84

# QUARTILES NUMPY

f_quart = np.percentile(sample_np, 25)
median = np.percentile(sample_np, 50)
th_quart = np.percentile(sample_np, 75)
print(f'First quartile(25%) is {f_quart}, second quartile(median, 50%) '
      f'is {median}, third quartile(75%) is {th_quart}')  # First quartile(25%) is 167.0, second quartile(median, 50%) is 170.5, third quartile(75%) is 173.0

# BOX-PLOT GRAPH

plt.boxplot(sample_np, showfliers=1)
plt.show()
