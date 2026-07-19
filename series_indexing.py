import pandas as pd 
x=pd.Series([23,43,44,55,61,10])
print(x[1])

# slicing 
from read_csv import s
print(s[5:16])
# negative slicing
print(s[-5:16])
print(s[::2])

# fancy indexing 
print(s[[1,3,4,5]])





