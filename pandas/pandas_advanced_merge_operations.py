import pandas as pd

df1 = pd.DataFrame({'calisanlar': ['Ali', 'Veli', 'Ayse', 'Fatma'],
                    'grup': ['Muhasebe', 'Muhendislik', 'Muhendislik', 'İK']})


df2 = pd.DataFrame({'calisanlar': ['Ayse', 'Ali', 'Veli', 'Fatma'],
                    'ilk_giris': [2010, 2009, 2014, 2019]})
print(df2)

print(pd.merge(df1, df2))

print(pd.merge(df1, df2, on = "calisanlar"))

df3 = pd.merge(df1, df2)
print(df3)


df4 = pd.DataFrame({'grup': ['Muhasebe', 'Muhendislik', 'İK'],
                    'mudur': ['Caner', 'Mustafa', 'Berkcan']})


print(df4)
print(pd.merge(df3,df4))

df5 = pd.DataFrame({'grup': ['Muhasebe', 'Muhasebe',
                              'Muhendislik', 'Muhendislik', 'İK', 'İK'],
                    'yetenekler': ['matematik', 'excel', 'kodlama', 'linux',
                               'excel', 'yonetim']})


print(df5)


print(df1)
print(pd.merge(df1, df5))
print()



















