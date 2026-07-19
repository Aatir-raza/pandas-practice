# using indexing 
import pandas as pd
from series_from_dict import marks
a=pd.Series(marks)
marks=pd.Series(marks)
marks.iloc[0]=90
print(marks)
 
 # what if index does not exist 
s=marks[1]=100
print(s)

# slicing 
from read_csv import s
a=s[2:4]=[100,100]
print(a)
