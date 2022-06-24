import joblib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model

data = {
    "area":[2200,2400,3500,2600,2800,2500,3000,3100,3300],
    "price":[5000000,5465000,7200000,5960000,6320000,5730000,6570000,6790000,7045000]
     }
df = pd.DataFrame(data)
print(df)
reg = linear_model.LinearRegression()
reg.fit(df[['area']] , df.price)
print(reg.coef_)
print(reg.intercept_)
print(reg.predict([[3300]]))
plt.xlabel('area(sq. ft)')
plt.ylabel('price (USD)')
plt.scatter(df.area, df.price, color='red',marker='*')
plt.plot(df.area, reg.predict(df[['area']]), color='green')
import joblib as jb
jb.dump(reg,'model_joblib')
mj = jb.load('model_joblib')
mj.predict([[3300]])