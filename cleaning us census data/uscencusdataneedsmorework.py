import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

us_cencus_files=glob.glob('C:\codecademy\Cleaning US Census Data\\states*.csv')


df_list=[]
for filename in us_cencus_files:
  data=pd.read_csv(filename)
  df_list.append(data)

us_cencus = pd.concat(df_list)
print(us_cencus.head(10))

#looking through the data

print(us_cencus.columns)
print(us_cencus.dtypes)

#changing income dtype

us_cencus['Income']=us_cencus['Income'].replace('[\$,]','',regex=True)
us_cencus.Income=pd.to_numeric(us_cencus['Income'])

print(us_cencus.dtypes)

#changing gender pop

split_gender=us_cencus['GenderPop'].str.split('_')
us_cencus['Men']=split_gender.str.get(0)
us_cencus['Women']=split_gender.str.get(1)

us_cencus['Men']=us_cencus['Men'].replace('M','',regex=True)
us_cencus['Women']=us_cencus['Women'].replace('F','',regex=True)
us_cencus.Men=pd.to_numeric(us_cencus['Men'])
us_cencus.Women=pd.to_numeric(us_cencus['Women'])
print(us_cencus.head(5))

##making the scatterplot

plt.scatter('Men','Women',data=us_cencus)
plt.show()
plt.clf()

plt.scatter('Women','Income',data=us_cencus)
plt.show()
plt.clf()

#filling na 

us_cencus = us_cencus.fillna(value={"Women":us_cencus['TotalPop']-us_cencus['Men']})
print(us_cencus['Women'])

old_df=us_cencus.duplicated()
print(old_df)


plt.scatter('Men','Women',data=us_cencus)
plt.show()
plt.clf()

plt.scatter('Women','Income',data=us_cencus)
plt.show()
plt.clf()
