
rows1 = int(input("Enter the number of rows for matrix 1: "))
columns1 = int(input("Enter the number of columns for matrix 1: "))
matrix1 = []
print("Enter the elements of matrix 1:")
for i in range(rows1):
    row = []
    for j in range(columns1):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
    matrix1.append(row)

rows2 = int(input("Enter the number of rows for matrix 2: "))
columns2 = int(input("Enter the number of columns for matrix 2: "))
matrix2 = []
print("Enter the elements of matrix 2:")
for i in range(rows2):
    row = []
    for j in range(columns2):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
    matrix2.append(row)

if rows1 != rows2 or columns1 != columns2:
    print("Matrix dimensions must be the same for addition and subtraction")
else:
    addition_result = []
    for i in range(rows1):
        row = []
        for j in range(columns1):
            row.append(matrix1[i][j] + matrix2[i][j])
        addition_result.append(row)

    
    subtraction_result = []
    for i in range(rows1):
        row = []
        for j in range(columns1):
            row.append(matrix1[i][j] - matrix2[i][j])
        subtraction_result.append(row)

    print("Matrix dimensions for addition and subtraction:")
    print(f"Matrix 1: {rows1}x{columns1}")
    print(f"Matrix 2: {rows2}x{columns2}")
    print()

    
    print("Addition:")
    for row in addition_result:
        print(row)
    print()

    print("Subtraction:")
    for row in subtraction_result:
        print(row)
    print()

if columns1 != rows2:
    print("Number of columns in matrix 1 must match the number of rows in matrix 2 for multiplication")
else:
    
    multiplication_result = []
    for i in range(rows1):
        row = []
        for j in range(columns2):
            element = 0
            for k in range(columns1):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        multiplication_result.append(row)


    print("Multiplication:")
    for row in multiplication_result:
        print(row)
    print()

transpose_result = []
for j in range(columns1):
    row = []
    for i in range(rows1):
        row.append(matrix1[i][j])
    transpose_result.append(row)


print("Transpose of matrix 1:")
for row in transpose_result:
    print(row)
