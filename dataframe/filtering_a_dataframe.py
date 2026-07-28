# find all the final winners
import pandas as pd 
a=(pd.read_csv(r"C:\Users\Homes\Desktop\PANDAS\dataframe\ipl-matches.csv"))
mask=a['MatchNumber']=='Final'
new_df=a[mask]
print(new_df[['Season','WinningTeam']])

# how many super over finishes have occured
b=a[a['SuperOver']=='Y'].shape[0]
print(b)

# how many matches has csk won in kolkata
c=a[(a['City']=='Kolkata') & (a['WinningTeam'] == 'Chennai Super Kings')].shape
print(c)
 # toss winner is match winner in percentage
A=(a[a['TossWinner']== a['WinningTeam']].shape[0]/a.shape[0])*100
print(A)




