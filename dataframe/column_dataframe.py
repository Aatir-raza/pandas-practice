import pandas as pd 
students_dicts={
  'name':['aatir','shahzada','aakash','almash'],
  'iq':[20,30,292,74],
  'marks':[78,34,43,54],
  'package':[43,434,435,56]
}
student=pd.DataFrame(students_dicts)
print(student)
student.set_index('name',inplace=True)
print(student)