import pandas as pd 
a=pd.read_csv(r"C:\Users\Homes\Desktop\PANDAS\Series\kohli_ipl.csv")
print(a)
# between
b= a[a['runs'].between(50,99)].size
print(b)

# clip
c=pd.read_csv(r"C:\Users\Homes\Desktop\PANDAS\Series\subs.csv")
print(c)
# clip
df=c.clip(100,200)
print(df)

# drop duplicates
temp=pd.Series([1,1,2,2,3,3,4,4])
d=temp.drop_duplicates()
print(d)

f=temp.duplicated().size
print(f)

#ISNULL
A=a.isnull().sum()
print(A)
# dropna
t=temp.dropna()
print(t)

# fillna  filling missing value any number like (2)
T=temp.fillna(7)
print(T)


