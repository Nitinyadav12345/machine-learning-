import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("sample.csv")
print(df)
md = math.floor(df.bedrooms.median())
df.bedrooms = df.bedrooms.fillna(md)
print(df)
reg = linear_model.LinearRegression()
reg.fit(df[['age']] , df.price)
print(reg.intercept_)
print(reg.coef_)
reg.predict([[3]])