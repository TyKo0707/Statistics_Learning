import numpy as np
from scipy import stats
import pandas as pd

sample_np = np.array([185, 175, 170, 169, 171, 175, 157, 172, 170, 172, 167, 173, 168, 167, 166,
                      167, 169, 172, 177, 178, 165, 161, 179, 159, 164, 178, 172, 170, 173, 171])

sample_pd = pd.Series([185, 175, 170, 169, 171, 175, 157, 172, 170, 172, 167, 173, 168, 167, 166,
                       167, 169, 172, 177, 178, 165, 161, 179, 159, 164, 178, 172, 170, 173, 171])

print('sorted array:', sorted(sample_np), sorted(sample_pd))
'''[157, 159, 161, 164, 165, 166, 167, 167, 167, 168, 169, 169, 170, 170, 170, 
    171, 171, 172, 172, 172, 172, 173, 173, 175, 175, 177, 178, 178, 179, 185]'''

# SCIPY and NUMPY
print('mode scipy:', stats.mode(sample_np))  # mode: ModeResult(mode=array([172]), count=array([4]))
print('median numpy:', np.median(sample_np))  # median: 170.5
print('mean numpy:', np.mean(sample_np))  # mean: 170.4

# PANDAS
print('mode pandas:', sample_pd.mode())  # mode pandas: 172
print('median pandas:', sample_pd.median())  # median pandas: 170.5
print('mean pandas:', sample_pd.mean())  # mean pandas: 170.4
