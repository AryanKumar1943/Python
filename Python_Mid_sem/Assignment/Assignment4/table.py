import math
print("a\tb\tpow(a,b)")
for a,b in (zip(range(1,6),range(2,7))):
    x=int(math.pow(a,b))
    print(f"{a}\t{b}\t{x}")