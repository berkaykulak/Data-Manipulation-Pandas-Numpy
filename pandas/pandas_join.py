import numpy as np
import pandas as pd
m = np.random.randint(1,30, size = (5,3))
df1 = pd.DataFrame(m, columns = ["var1","var2","var3"])


print(df1)
df2 = df1 + 99
print(df2)

print(pd.concat([df1,df2]))


print(pd.concat([df1,df2], ignore_index=True))
print(df1.columns)

df2.columns = ["var1","var2","deg3"]

print(df2)
print(df1)

print(pd.concat([df1, df2]))
print(pd.concat([df1, df2], join = "inner"))
print(pd.concat([df1, df2], join_axes = [df2.columns], ignore_index=True))
print()
print()