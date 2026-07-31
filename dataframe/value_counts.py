import pandas as pd 
import matplotlib.pyplot as plt
a=pd.read_csv(r'C:\Users\Homes\Desktop\PANDAS\dataframe\ipl-matches.csv')

# find which player has won potm in finals and qualifier
b=a[~a['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts()
print(b)

# toss decision plot
c=a['TossDecision'].value_counts().plot(kind='pie')
print(c)
plt.show()

# how many matches each team has played (how many times occur in team 1 and team 2 )
d=(a['Team1'].value_counts()+ a['Team2'].value_counts()).sort_values(ascending=False)
print(d)
