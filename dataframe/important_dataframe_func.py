import pandas as pd 
a=(pd.read_csv(r"C:\Users\Homes\Desktop\PANDAS\dataframe\ipl-matches.csv"))
a.info()
#astype is use for memory reduce the address of datasets
a['ID']=a['ID'].astype('int32')
print(a['ID'])
b=a['Season'].astype('category')
print(b)
