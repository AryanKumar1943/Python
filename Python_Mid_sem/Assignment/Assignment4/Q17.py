s=int(input("Enter size of size"))
print("Enter the entries of list :")
l=[]
for i in range(s):
    l.append(int(input()))

for i in range(s):
    if(l[i]>l[i+1]):
        print("not sorted") 
          

