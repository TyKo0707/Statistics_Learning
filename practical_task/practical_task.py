import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

data = []

with open('states.csv', newline='') as file:
    reader = csv.reader(file)
    for elem in enumerate(reader):
        if elem[0] != 0:
            data.append([float(elem[1][3]), float(elem[1][4])])

data.sort()
data = np.array(data)

# slope - b1, intercept - b0, r - coefficient of correlation,
# p - p-value for a hypothesis, std_err - standard error of the estimated slope
slope, intercept, r, p, std_err = linregress(data[:, 0], data[:, 1])

x = np.linspace(75, 100)
reg = lambda x: intercept + slope * x

plt.figure(figsize=(25, 10), dpi=80)
plt.scatter(data[:, 0], data[:, 1])
plt.title('Linear Regression')
plt.plot(x, reg(x), color='r', label='fitted line')
plt.legend()
print(f'''
slope = {slope:.2f}
intercept = {intercept:.2f}
r = {r:.2f}
r squared = {(r ** 2):.2f}
p = {p:.5f}
std_err = {std_err:.3f}
''')
plt.show()
