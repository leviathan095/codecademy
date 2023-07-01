import scipy.stats as stats
import numpy as np

lam = 7

print(stats.poisson.pmf(lam , lam))

very_good_day = stats.poisson.cdf(4,lam)
print(very_good_day)
very_bad_day = 1 - stats.poisson.cdf(9,lam)
print(very_bad_day)

year_defects = stats.poisson.rvs(lam, size=365)
# print(year_defects)

print(year_defects[:20])
print(365 * lam)
print(year_defects.sum())
print(year_defects.mean())

max_defect = year_defects.max()
print(max_defect)

max_defect_prob = 1 - stats.poisson.cdf(max_defect, lam)
print(max_defect_prob)

ninety_percent_days = stats.poisson.ppf(0.9, lam)
print(ninety_percent_days)

