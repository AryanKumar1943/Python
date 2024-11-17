from itertools import permutations

s="car"
l=[]
for p in permutations(s):
    l.append(''.join(p))

   
print(l)
