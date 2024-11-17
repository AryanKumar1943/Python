a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("rnter the value of c:"))
maximum=max(a,b,c)
minimum=min(a,b,c)
mid=(a+b+c)-maximum-minimum
print(f"maximum of the three is {maximum}")
print(f"minimum  of the three string is {minimum}")
print(f"middle element is {mid}")