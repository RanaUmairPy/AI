import pandas as pd


df = pd.read_csv('seattle-weather.csv')
df.fillna(1, inplace=True)
#print(df)
x = df[['seattle-weather.csv date','weather','wind']]
#print(x)
x1 = df[['weather']]
#print(x1)
x.to_csv("newfile.csv")
x1.to_csv("newfile2.csv")

y = pd.read_csv('newfile.csv')
print(y)
z = pd.read_csv('newfile2.csv')
print(z)

#concatenate
result = pd.concat([y,z], axis=1)
print(result)

result.to_csv("finalfile.csv")