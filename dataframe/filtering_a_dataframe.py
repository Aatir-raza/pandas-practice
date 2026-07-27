import pandas as pd 
a=(pd.read_csv(r"C:\Users\Homes\Desktop\PANDAS\dataframe\ipl-matches.csv"))
mask=a['MatchNumber']=='Final'
new_df=a[mask]
print(new_df[['Season','WinningTeam']])
