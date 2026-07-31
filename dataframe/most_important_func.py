import pandas as pd 
marks=pd.DataFrame([
  [100,80,10],
  [90,70,7],
  [120,100,14],
  [80,70,14],
  [80,70,14]
], columns=['iq','marks','package'])
print(marks)
a=marks.value_counts
print(a)
