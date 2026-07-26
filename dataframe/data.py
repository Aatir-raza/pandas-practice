import pandas as pd 
# using list
students_data=[
  [100,20,6],
  [200,5,7],
  [400,70,7],
  [499,80,20]
]
print(pd.DataFrame(students_data,columns=['iq','marks','package']))
#using dicts
import pandas as pd 
students_dicts={
  'iq':[20,30,292,74],
  'marks':[78,34,43,54],
  'package':[43,434,435,56]
}
a=pd.DataFrame(students_dicts)
print(a)

# using read csv
s=(pd.read_csv( r"C:\Users\Homes\Desktop\PANDAS\dataframe\movies.csv"))
print(s)
