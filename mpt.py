import joblib as jb
md = jb.load('model_joblib')
print(md.predict([[3300]]))

