# -*- coding: utf-8 -*-
import pickle
import pandas as pd

#%%
df = pd.read_csv('ml/농림축산식품부_낙농체험 목장 정보_20151231.csv', encoding='cp949')
    
#%%
farms = dict(zip(df['목장명'], df['주소']))
sorted_farms = sorted(farms.items(), key = lambda item: item[0])

#%%
result = {}
for i in range(len(sorted_farms)) :
    result[sorted_farms[i][0]] = sorted_farms[i][1]

#%%
with open('ml/farm.p', 'wb') as f:
    pickle.dump(result, f)

#%%
with open("ml/farm.p","rb") as fr:
    data = pickle.load(fr)

#%%
print(data)
