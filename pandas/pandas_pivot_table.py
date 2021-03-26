import pandas as pd
import seaborn as sns
titanic = sns.load_dataset('titanic')
titanic.head()


print(titanic.groupby("sex")[["survived"]].mean())
print(titanic.groupby(["sex","class"])[["survived"]].aggregate("mean").unstack())
print(titanic.pivot_table("survived", index = "sex", columns = "class"))
print(titanic.age.head())
print(titanic.pivot_table("survived", ["sex", age], "class"))
print()