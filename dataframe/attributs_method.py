# dataframe attributes and method
from data import s,a
import pandas as pd 
print(s.shape)
print(s.dtypes)
print(s.index)
print(s.columns)
print(s.values)
print(s.head(2))
print(s.tail(2))
print(s.sample(5))
print(s.info())
print(s.describe())
print(s.isnull().sum())
print(s.duplicated())
a.rename(columns={'marks':'percent','package':'lpa'},inplace=True)
print(a)
