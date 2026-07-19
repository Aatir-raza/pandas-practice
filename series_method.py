from read_csv import subs,s
# head and tails 
print(subs.head())
print(s.tail)
# sample
print(s.sample(5))
# values_counts
print(s.value_counts())
#sort_values->inplace
print(s.sort_values())
print(s.sort_values(inplace=True))

# sort_index
print(s.sort_index(inplace=True))
print(s.sort_index(ascending=False,inplace=True))

