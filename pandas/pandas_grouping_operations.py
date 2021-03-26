import pandas as pd
import seaborn as sns

df = pd.DataFrame({'gruplar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'veri': [10,11,52,23,43,55]}, columns=['gruplar', 'veri'])

print(df)

print(df.groupby("gruplar"))
print(df.groupby("gruplar").mean())
print(df.groupby("gruplar").sum())
df = sns.load_dataset("planets")

print(df.head())
print(df.groupby("method"))
print(df.groupby("method")["orbital_period"].mean())
print(df.groupby("method")["orbital_period"].describe())
print()

