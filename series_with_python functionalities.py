from read_csv import subs
# len/type/dir/sorted/max/min
print(len(subs))
print(type(subs))
print(dir(subs))
print(sorted(subs))
print(min(subs))
print(max(subs))

# tyoe conversion
print(list(subs))
print(dict(subs))

# memebership operator 
print(subs)
print(360 in subs)
print(4000 in subs)

# lopping
for i in subs.index:
  print(i)
# Arithmetic operator 
print(100-subs)  
# relational operator
print(subs>=50)

