a=int(input("Enter the number"))
l=[]
for i in str(a):
    l.append(i)
   
l.sort();
print("first Greatest digit is :",l[len(l)-1])
print("Second gretest digit is :",l[len(l)-2])
print("third Greatest digit is :",l[len(l)-3])


