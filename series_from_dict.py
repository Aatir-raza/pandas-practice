import pandas as pd
marks={
  'python':100,
  'cpp':77,
  'cn':67,
  'os':70
  }
s=pd.Series(marks,name='aatir ke marks')
print(s)

# series attributes
# size
print(s.size)

# dtype
print(s.dtype)
# name
print(s.name)
# is_unique
print(s.is_unique)
# index
print(s.index)
# values
print(s.values)



