from correlation.correlation import y1, x, cor  # the module in the same directory
import matplotlib.pyplot as plt

b1 = y1.std() / x.std() * cor(x, y1)
b0 = y1.mean() - b1 * x.mean()
f_x = lambda x: b0 + b1 * x
y_pred = f_x(x)
plt.scatter(x, y1)
plt.plot(x, y_pred, color='r')
plt.show()
