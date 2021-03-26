import pandas as pd

pd.Series([10,88,3,4,5])

seri = pd.Series([10,88,3,4,5])

print(type(seri))
print(seri.axes)
print(seri.dtype)
print(seri.size)
print(seri.ndim)
print(seri.values)
print(seri.head(3))
print(seri.tail(3))
print(pd.Series([99,22,332,94,5]))
print(pd.Series([99,22,332,94,5], index = [1,3,5,7,9]))
print(pd.Series([99,22,332,94,5], index = ["a","b","c","d","e"]))


seri = pd.Series([99,22,332,94,5], index = ["a","b","c","d","e"])
print(seri["a"])
print(seri["a":"c"])

sozluk = {"reg":10, "log":11, "cart": 12}
seri = pd.Series(sozluk)
print(seri)
print(pd.concat([seri,seri]))









