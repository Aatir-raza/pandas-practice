import pandas as pd 
b=(pd.read_csv( r"C:\Users\Homes\Desktop\PANDAS\dataframe\movies.csv"))
print(b)
# single cols
print(b['title_x'])
# multiple cols
print(b[['title_x','year_of_release','actors']])