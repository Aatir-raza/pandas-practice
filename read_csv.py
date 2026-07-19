import pandas as pd 
subs=pd.read_csv ( r"C:\Users\Homes\Desktop\PANDAS\subs.csv").squeeze('columns')
print(subs)  
print(type(subs)) 


import pandas as pd 
s=pd.read_csv ( r"C:\Users\Homes\Desktop\PANDAS\kohli_ipl.csv",index_col='match_no').squeeze('columns')
print(s)  
print(type(s)) 


