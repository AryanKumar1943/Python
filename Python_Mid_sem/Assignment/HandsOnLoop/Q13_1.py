x = 5
while(x != 0):
    y = 5  # Reset y to 5 for each iteration of the outer loop
    while(y != 0):
        print("*", end=" ")
        y -= 1
    print()  # To print a newline after each row of stars
    x -= 1
