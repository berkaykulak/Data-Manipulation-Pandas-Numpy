import numpy as np
import pandas as pd
m = np.random.randint(1,30, size = (10,3))
df = pd.DataFrame(m, columns = ["var1","var2","var3"])


print(df)
print(df["var1"])
print(df[0:2][["var1","var2"]])
print(df)
print(df.var1)
print(df[df.var1 > 15])

print(df[(df.var1 > 15) & (df.var3 < 5)])
print(df.loc[(df.var1 > 15), ["var1","var2"]])
print(df[(df.var1 > 15)][["var1","var2"]])
