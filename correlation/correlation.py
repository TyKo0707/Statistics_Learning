import numpy as np
import random
import matplotlib.pyplot as plt


def cov(x, y):
    # the same as "if (x.size == y.size) else 'Samples must have same size'"
    assert x.size == y.size, 'Samples must have same size'
    return ((x - x.mean()) * (y - y.mean())).sum() / (x.size - 1)


def cor(x, y):
    return cov(x, y) / (np.std(x, ddof=1) * np.std(y, ddof=1))


# function simulating random factors
def randomize(arr, p):
    alpha = np.max(arr) - np.min(arr)
    res = np.zeros(arr.shape)
    for i, v in enumerate(arr):
        sign = 1 if random.choice([True, False]) else -1
        res[i] = v + sign * alpha * random.random() * p
    return res


x = np.array(range(30))
y = randomize(x, 0.1)
y1 = randomize(x, 0.5)
y2 = randomize(x, 1)

if __name__ == "__main__":
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 3))
    ax1.scatter(x, y)
    ax2.scatter(x, y1)
    ax3.scatter(x, y2)
    ax1.set_title('High correlation')
    ax2.set_title('Medium correlation')
    ax3.set_title('Low correlation')

    print(f'''
    cov1: {cov(x, y):.2f}
    cov2: {cov(x, y1):.2f}
    cov3: {cov(x, y2):.2f}
    
    cor1: {cor(x, y):.2f}
    cor2: {cor(x, y1):.2f}
    cor3: {cor(x, y2):.2f}
    ''')

    plt.show()
