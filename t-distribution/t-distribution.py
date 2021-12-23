"""
The graph below shows how the shape of the distribution changes with an increase in the number of degrees of freedom.
It also shows the approach of the t-distribution to the normal one as the degrees of freedom increase
"""
from scipy.stats import t, norm
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y1, y2, y3 = t.pdf(x, df=1), t.pdf(x, df=3), t.pdf(x, df=10)
y4 = norm.pdf(x)

plt.title('T-distribution plots with different degrees of freedom')
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4, 'r:')
plt.legend(('df=1', 'df=3', 'df=10', 'norm'))
plt.show()

'''
On a sample of 15 observations using a one-sample t-test
the null hypothesis is tested: μ = 10
and the calculated t-value is -2 (t = -2), then the p-level of significance (two-sided) is: 
'''
from scipy import stats

t = -2
n = 15
df = n - 1

p = 2 * stats.t.sf(abs(t), df)
print(f'p = {p:.3f}')  # p = 0.065
