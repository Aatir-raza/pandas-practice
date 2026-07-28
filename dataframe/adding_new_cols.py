import pandas as pd 
b=pd.read_csv( r'C:\Users\Homes\Desktop\PANDAS\dataframe\movies.csv')
print(b)
# adding new columns
b['country']='India'
print(b.head)
print(b.head())
print(b.columns)

# from existing ones
b.dropna(inplace=True)
b['lead actor']=b['actors'].str.split('|').apply(lambda x:x[0])
print(b['lead actor'])