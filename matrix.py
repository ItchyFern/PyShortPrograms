# Used to help understand how matricies work when attempting to figure
# out how to do the same operations in MIPS. lesson learned... Python is
# always a better choice :p

A=[]
A.append([2,1,9,2])
A.append([7,9,10,10])
A.append([3,4,4,4])
A.append([2,5,4,4])
B=[]
B.append([8,7,1,2])
B.append([2,7,8,6])
B.append([7,5,6,8])
B.append([9,4,8,9])

def add(A, B):
    C=[]
    for x in range (4):
        temp=[]
        for y in range (4):
            temp.append(A[x][y]+B[x][y])
        C.append(temp)
    return C

def mul(A, B):
    C=[]
    for x in range(4):
        temparr=[]
        for y in range (4):
            tempint=0
            for z in range (4):
                tempint+=A[x][z]*B[z][y]
            temparr.append(tempint)
        C.append(temparr)
    return C

def printMatrix(matrix):
    for x in range (4):
        for y in range (4):
            print (matrix[x][y],"\t", end='')
        print()

printMatrix(A)
print("\n\n")
printMatrix(B)
print("\n\n")
printMatrix(add(A, B))
print("\n\n")
printMatrix(mul(A, B))
