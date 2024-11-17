r1 = int(input("Enter the number of rows for matrix 1: "))
c1 = int(input("Enter the number of columns for matrix 1: "))
r2 = int(input("Enter the number of rows for matrix 2: "))
c2 = int(input("Enter the number of columns for matrix 2: "))

# Check if matrix multiplication is possible
if c1 != r2:
    print("Matrix multiplication is not possible. The number of columns in matrix 1 must be equal to the number of rows in matrix 2.")
else:
    # Input matrix 1
    matrix1 = []
    print("Enter the elements for matrix 1:")
    for row in range(r1):
        a = []
        for column in range(c1):
            a.append(int(input()))
        matrix1.append(a)

    # Display matrix 1
    print("Our matrix1 is:")
    for row in range(r1):
        for column in range(c1):
            print(matrix1[row][column], end=" ")
        print()

    # Input matrix 2
    matrix2 = []
    print("Enter the elements for matrix 2:")
    for row in range(r2):
        a2 = []
        for column in range(c2):
            a2.append(int(input()))
        matrix2.append(a2)

    # Display matrix 2
    print("Our matrix2 is:")
    for row in range(r2):
        for column in range(c2):
            print(matrix2[row][column], end=" ")
        print()

    # Initialize the result matrix (matrix3) with zeros
    matrix3 = [[0 for _ in range(c2)] for _ in range(r1)]

    # Perform matrix multiplication
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):  # or range(r2), as c1 == r2
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]

    # Display the result matrix (matrix3)
    print("Our result matrix (matrix3) is:")
    for row in range(r1):
        for column in range(c2):
            print(matrix3[row][column], end=" ")
        print()
