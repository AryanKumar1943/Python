# Python program to input 10 integers, search for a number, and display its count

# Input 10 integers from the user
num_list = []
print("Enter 10 integers:")
for i in range(10):
    num = int(input(f"Enter integer {i+1}: "))
    num_list.append(num)

# Input the number to be searched
search_num = int(input("Enter the number to search: "))

# Check if the number is present and display the count
count = num_list.count(search_num)

if count > 0:
    print(f"The number {search_num} is present in the list and appears {count} times.")
else:
    print(f"The number {search_num} is not present in the list.")
