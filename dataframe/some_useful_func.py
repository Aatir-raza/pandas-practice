import pandas as pd
a=pd.read_csv(r"C:\Users\Homes\Desktop\PANDAS\Series\kohli_ipl.csv")
print(a)
# isin 
b=a[a.isin([49,99])]
print(b)
c=a.head().copy()
print(c)
new=a.head().copy()
new[1]=100
print(new)
