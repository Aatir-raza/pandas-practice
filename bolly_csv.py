import pandas as pd 
movies=pd.read_csv( r"C:\Users\Homes\Desktop\PANDAS\bollywood.csv", encoding='latin1')
print(movies.head())  
print(type(movies))