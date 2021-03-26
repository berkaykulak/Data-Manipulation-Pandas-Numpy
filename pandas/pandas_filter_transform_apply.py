import pandas as pd
import numpy as np

df = pd.DataFrame({'gruplar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'degisken1': [10,23,33,22,11,99],
                   'degisken2': [100,253,333,262,111,969]},
                   columns = ['gruplar', 'degisken1', 'degisken2'])

print(df)
print(df.groupby("gruplar").mean())
print(df.groupby("gruplar").aggregate([min, np.median, max]))
print(df.groupby("gruplar").aggregate({"degisken1": "min", "degisken2": "max"}))


df = pd.DataFrame({'gruplar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'degisken1': [10,23,33,22,11,99],
                   'degisken2': [100,253,333,262,111,969]},
                   columns = ['gruplar', 'degisken1', 'degisken2'])

print(df)


def filter_func(x):
    return x["degisken1"].std() > 9

print(df.groupby("gruplar").std())

print(df.groupby("gruplar").filter(filter_func))

print(df["degisken1"]*9)
df_a = df.iloc[:,1:3]

print(df_a.transform(lambda x: (x-x.mean()) / x.std()))

print(df.apply(np.sum))
print(df.groupby("gruplar").apply(np.mean))







