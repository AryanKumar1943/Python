print("Hello,World!")
if 5>2:
    print("Five is greater than two!")

#print type
a=int(input("enter value of a:"))
print(a)
print(type(a))
# take multiple inputs in array
input_str_array = input().split()

print("array:", input_str_array)

# take multiple inputs in array
input_int_array = [int(x) for x in input().split()]

print("array:", input_int_array)
