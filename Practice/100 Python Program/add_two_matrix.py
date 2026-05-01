"""add two matrices"""
A = [[1,5,3],
     [3,4,2],
     [10,9,6]]
B = [[7,9,3],
     [6,7,9],
     [9,8,3]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range (len(A)):
    for j in range (len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

for r in result:
    print(r)
