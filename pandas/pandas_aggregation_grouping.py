import seaborn as sns
import pandas as pd
df = sns.load_dataset("planets")
print(df.head())

print(df.shape)
print(df.mean())
print(df["mass"].mean())
print(df["mass"].count())
print(df["mass"].min())
print(df["mass"].max())
print(df["mass"].sum())
print(df["mass"].std())
print(df["mass"].var())
print(df.describe().T)
print()


