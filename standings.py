import csv
import pandas as pd
df = pd.read_csv("standings.csv")

currentyear='2021-22'
df=df.loc[df['Season'] == currentyear]
df = df.iloc[:, 1:8]
print(df)

with open('./standings.txt', 'w') as f:
    dfAsString = df.to_string(header=False, index=False)
    f.write(dfAsString)