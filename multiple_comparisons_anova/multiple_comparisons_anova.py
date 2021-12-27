import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from scipy.stats import t


def pair_t(samples, alpha):
    # Pair t-test, if samples are equal, returns True
    n_samples = samples.shape[0]
    n_combinations = n_samples * (n_samples - 1) // 2
    result = np.zeros(n_combinations, dtype=bool)
    k = 0
    for i in range(n_samples):
        for j in range(i + 1, n_samples):
            N = samples[i].size
            std_err = np.sqrt((samples[i].std() ** 2) / N + (samples[j].std() ** 2) / N)
            t_value = (samples[i].mean() + samples[j].mean()) / std_err
            p = t.sf(t_value, N - 2)
            result[k] = p >= alpha
            k += 1
    return np.all(result)


def pair_t_test(repeat, n_samples, sample_size, ax, alpha=0.05):
    """
    The function shows how many False results we will have,
    when pairwise comparison of a set of samples using a t-test
    """
    result = np.zeros(repeat, dtype=bool)
    for i in range(repeat):
        samples = random.randn(n_samples, sample_size)
        result[i] = pair_t(samples, alpha)

    unique, counts = np.unique(result, return_counts=True)
    percentage = counts / result.size
    ax.pie(percentage, normalize=False, labels=unique, autopct='%.0f%%')


fig, axs = plt.subplots(ncols=4, figsize=(20, 4))
n_samples = [2, 4, 8, 16]
fig.suptitle('Error percent when pairwise comparison of a set of samples using a t-test: ')

for n, ax in zip(n_samples, axs):
    pair_t_test(1000, n, 100, ax)
    ax.set_title(f'{n} samples')

plt.show()
