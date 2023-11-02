def matrix_multiplication(a, b):
    if len(a[0]) != len(b):
        return None
    
    result = [[0 for j in range(len(b[0]))] for i in range(len(a))]
    
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    
    return result

a = ((1, 2, 3), (3, 2, 1))
b = ((1, 2), (3, 4), (5, 6))

result = matrix_multiplication(a, b)

if result is None:
    print("Las matrices no se pueden multiplicar")
else:
    for row in result:
        print(row)

#https://matrixcalc.org/es/#%7B%7B1,2,3%7D,%7B3,2,1%7D%7D*%7B%7B1,2%7D,%7B3,4%7D,%7B5,6%7D%7D