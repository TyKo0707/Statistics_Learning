from scipy import stats
import pandas as pd

# Samples to compare
data = pd.DataFrame({
    'a': [3, 1, 2],
    'b': [5, 3, 4],
    'c': [7, 6, 5]
})
data.boxplot()
print('Null hypothesis: ', '='.join(data))
print('Alternative hypothesis: ', f'!({"=".join(data)})')
# Total average
grand_mean = data.values.flatten().mean()  # .flatten() - Return a copy of the array collapsed into one dimension
# deviation of the group average from the total average
ssb = sum(data[group].size * (group_mean - grand_mean) ** 2 for group, group_mean in data.mean().items())
# deviations of values within the group from the average group
ssw = sum(sum((x - group_mean) ** 2 for x in data[group]) for group, group_mean in data.mean().items())

groups = data.shape  # .shape() - Return a tuple representing the dimensionality of the DataFrame
print(groups)  # (3, 3)
dfb = groups[1] - 1
dfw = data.size - groups[1]
# SSB
mssb = ssb / dfb
# SSW
mssw = ssw / dfw

f_value = mssb / mssw

p = stats.f.sf(f_value, dfb, dfw)
print('Result:')
if p < 0.05:
    print('Reject the null hypothesis ')
else:
    print('NOT reject the null hypothesis ')
