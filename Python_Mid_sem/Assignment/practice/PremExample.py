from itertools import permutations
s="car"
prem=permutations(s)
l=[]
for i in prem:
    l.append("".join(i))

print(l)