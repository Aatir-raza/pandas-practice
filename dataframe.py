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
print(pd.DataFrame(students_dicts))

# using read_csv
print(pd.read_csv("C:\\Users\\Homes\\Desktop\\PANDAS\\movies.csv"))