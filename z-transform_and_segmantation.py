"""
Считается, что значение IQ (уровень интеллекта) у людей имеет нормальное распределение
со средним значением равным 100 и стандартным отклонением равным 15 (M = 100, sd = 15).
Какой приблизительно процент людей обладает IQ > 125?
"""

from scipy import stats

mean = 100
std = 15
IQ = 125
# sf - Survival function = (1 - cdf) - Cumulative distribution function
print(f"Only {(stats.norm(mean, std).sf(IQ)) * 100:.2f}% of all people have IQ more than {IQ}")  # Only 4.78% of all people have IQ more than 125
