
A = [ [7, 8, 9, 7],
      [2, 7, 9, 7],
      [8, 6, 7, 2],
      [5, 6, 7, 8] ]

B = [ [8, 3, 2, 6],
      [8, 9, 10, 3],
      [2, 9, 4, 2],
      [9, 3, 6, 2] ]

output_C = [ [0, 0, 0,0],
             [0, 0, 0,0],
             [0, 0, 0,0],
             [0, 0, 0, 0] ]

for i in range(0,4):
    for j in range(0,4):
        for k in range(0,4):
            output_C[i][j] += A[i][k]*B[k][j]

for p in output_C:
    print(p)
