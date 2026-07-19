# string
import numpy as np
import pandas as pd
country=['india','pakistan','Iran','palestine']
print(pd.Series(country))

# integer
run=[57,67,100,77]
print(pd.Series(run))

# custom index
marks=[57,67,100,77]
subject=['hindi','english','maths','python']
print(pd.Series(marks,index=subject))

# setting a name 
marks=pd.Series(marks,index=subject,name='Aatir ka marks')
print(marks)
print(marks.subs)