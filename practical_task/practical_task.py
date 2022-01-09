import csv
import numpy as np
import matplotlib.pyplot as plt
from correlation.correlation import cov, cor

data = []

with open('states.csv', newline='') as file:
    reader = csv.reader(file)
    for elem in enumerate(reader):
        if elem[0] != 0:
            data.append([float(elem[1][3]), float(elem[1][4])])

data.sort()
data = np.array(data)

plt.figure(figsize=(25, 10), dpi=80)
plt.scatter(data[:, 0], data[:, 1])
plt.show()
