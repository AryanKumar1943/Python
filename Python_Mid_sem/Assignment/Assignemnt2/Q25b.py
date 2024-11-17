x = 5
for i in range(5):
    # Print leading spaces
    for j in range(x - i - 1):
        print(" ", end="")
        
    # Print asterisks
    for k in range(i + 1):
        print("*", end="")
        
    print()  # Move to the next line
