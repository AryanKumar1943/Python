days=(int(input("enter number of days:")))
hours=(int(input("enter hours:")))
minutes=(int(input("enter minutes:")))
seconds=(int(input("enter seconds:")))
answer=(days*24*60*60)+(hours*60*60)+(minutes*60)+seconds
print(f"the total number of seconds is {answer}")