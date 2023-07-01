
import math
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt

## Read in Data
flight = pd.read_csv("C:\codecademy\Airline Analysis\\flight.csv")
print(flight.head())

## Task 1
print(np.mean(flight.coach_price))
print(np.median(flight.coach_price))

sns.histplot(flight.coach_price)
plt.show()
plt.clf()

##Task 2
print(np.mean(flight.coach_price[flight.hours == 8]))
print(np.median(flight.coach_price[flight.hours == 8]))

sns.histplot(flight.coach_price[flight.hours == 8])
plt.show()
plt.clf()

##Task 3
print(np.mean(flight.delay))
print(np.median(flight.delay))

sns.histplot(flight.delay[flight.delay <500])
plt.show()
plt.clf()


##Task 4
percent=0.01
flight_sub = flight.sample(n=int(flight.shape[0]* percent))
sns.lmplot(x='coach_price', y='firstclass_price', data= flight_sub)
plt.show()
plt.clf()

##Task 5

sns.histplot(flight,x= 'coach_price', hue=flight.inflight_meal)
plt.show()
plt.clf()


sns.histplot(flight,x= 'coach_price',hue=flight.inflight_entertainment)
plt.show()
plt.clf()

sns.histplot(flight,x= 'coach_price' ,hue=flight.inflight_wifi)
plt.show()
plt.clf()


##Task 6

sns.lmplot(x='hours',y='passengers',data=flight, x_jitter=.23,scatter_kws={"s": 5, "alpha":0.2}, fit_reg = False )
plt.show()
plt.clf()

##Task 7
sns.histplot(flight,x='coach_price',y='firstclass_price',hue=flight.weekend)
plt.show()
plt.clf()

##Task 8

sns.boxplot(x='day_of_week,y=''coach_price',hue='redeye',data=flight)
plt.show()
plt.clf()


