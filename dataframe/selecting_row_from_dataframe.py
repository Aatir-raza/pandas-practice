import pandas as pd 
c=(pd.read_csv( r"C:\Users\Homes\Desktop\PANDAS\dataframe\movies.csv"))
# single row
print(c.iloc[0])
# multiple row 
print(c.iloc[0:5])

# fancy indexing
print(c.iloc[[0,4,5]])

# loc
students_dicts={
  'name':['aatir','shahzada','aakash','almash'],
  'iq':[20,30,292,74],
  'marks':[78,34,43,54],
  'package':[43,434,435,56]
}
df=pd.DataFrame(students_dicts)
print(df[df['name']=='aatir'])

# selecting both rows and cols
print(c.iloc[0:3,0:3])
print(c.loc[0:2,'title_x':'poster_path' ])





