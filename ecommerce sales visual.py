
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv(r"C:\Users\princ\OneDrive\문서\practice folder\ecommerce.csv")


data.groupby('City')['Price'].sum().plot(kind='bar')

plt.show()
group_data=data.groupby('Category')['Price'].sum().plot(kind='pie')
plt.show()

data.groupby('Category')['OrderID'].count().plot(kind='bar', color=['red','green','blue'])
plt.show()

data_group=data.groupby(['City','Category'])['Price'].sum().plot(kind='line')
data_group['Alexandria'].plot(kind='bar')
plt.show()

a=data.groupby('City').agg(
 total_sales=('Price','sum'),
 avg_sales=('Price','mean'),
 orders=('Price','count')   
).plot(kind='bar')
plt.show()

print(data)
print(a)