import pandas as pd 
a=pd.read_csv( r'C:\Users\Homes\Desktop\PANDAS\dataframe\movies.csv')
print(a)
condition=a[(a['imdb_rating'] > 8) & (a['imdb_votes'] > 10000)].shape
print(condition)

# action movies rating  higher 7.5
s=a['genres'].str.contains('Action')
d=a['imdb_rating']>7.5
print(s&d)