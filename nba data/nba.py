import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('C:\codecademy\Codecademy_NBA_Trends_Project\Codecademy_NBA_Trends_Project\\nba_games.csv')

nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())
print(nba.info())
knicks_pts_10 = nba_2010[nba_2010.fran_id == 'Knicks']['pts']
nets_pts_10 = nba_2010[nba_2010.fran_id == 'Nets']['pts']

print(knicks_pts_10)
print(nets_pts_10)

diff_points_mean_10 = knicks_pts_10.mean() - nets_pts_10.mean()
print(diff_points_mean_10)

plt.hist(knicks_pts_10, label="Knicks Points'10", color='red',alpha=0.5)
plt.hist(nets_pts_10,label="Nets Points'10",color='blue',alpha=0.5)
plt.legend()
plt.title('2010 Season')
plt.show()

knicks_pts_14 = nba_2014[nba_2014.fran_id == 'Knicks']['pts']
nets_pts_14 = nba_2014[nba_2014.fran_id == 'Nets']['pts']

diff_points_mean_14 = knicks_pts_14.mean() - nets_pts_14.mean()
print(diff_points_mean_14)

plt.hist(knicks_pts_14,label="Knicks Points'14",color='red',alpha=0.8)
plt.hist(nets_pts_14,label="Nets Points'14",color='blue',alpha=0.8)
plt.legend()
plt.title('2014 Season')
plt.show()

sns.boxplot(data=nba_2010,x='fran_id',y='pts')
plt.show()


location_result_freq = pd.crosstab(nba_2010.game_result,nba_2010.game_location)
print(location_result_freq)

location_result_proportions = location_result_freq/len(nba_2010)
print(location_result_proportions)

chi2,pval,dof,expected = chi2_contingency(location_result_freq)

print(expected)
print(chi2)

print(np.cov(nba_2010.forecast,nba_2010.point_diff))

point_diff_forecast_corr,p = pearsonr(nba_2010.point_diff,nba_2010.forecast) 
print(point_diff_forecast_corr)

plt.scatter(x=nba_2010.forecast,y=nba_2010.point_diff)
plt.xlabel('Forecast')
plt.ylabel('Point Difference')
plt.show()