from functools import reduce
l=[1,2,3,4,5]
addl=reduce(lambda x,y : x+y,l)
print(addl)
#genertor
newl=(i**2 for i in [1,3])
print(list(newl))