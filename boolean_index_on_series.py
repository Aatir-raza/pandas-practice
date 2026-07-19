# find no of 50s and  100s scored by kohli 
from read_csv import s,subs
print(s[s>=50].size)
# find number of ducks
print(s[s==0].size)

# count no of day when I had more than 200 subs a day
print(subs[subs>200].size)

