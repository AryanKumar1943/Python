#Note: a string can be rearranged and converted to palindome only if the frequency of odd count chars are not more than 1
s="aman"
my_dict={}
for i in s:
    my_dict[i]=(my_dict.get(i,0))+1

oddcount=0
for i in my_dict.values():
    if(i%2!=0):
        oddcount=oddcount+1

if(oddcount>1):
    print("palindrom cant be formed")
else:
    print("palindrome can be formed")
