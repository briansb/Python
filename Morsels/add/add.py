
def add(m1, m2):
    if len(m1) != len(m2):
        return "Error - size mismatch"

    #z = [x+y for x in m1 for y in m2]
    #z = [x+y for x in m1 for y in m2 if matrix1.index(x) == matrix2.index(y)]
   
    result = m2
    
    for lst in m1:
        for element in lst:
            i = m1.index(lst)
            j = lst.index(element)
            result[i][j] += m1[i][j]


    return result


#----------------

matrix1 = [[1,-2],[-3,4]]
matrix2 = [[2,-1],[0,-1]]
print(matrix1)
print(matrix2)
print("-------------------")
print add(matrix1,matrix2)

print("\n\n")

matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
print(matrix1)
print(matrix2)
print("-------------------")
print add(matrix1,matrix2)


