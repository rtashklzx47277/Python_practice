import numpy as np
# import sys
# data = sys.stdin.read()
data = """2
2,3,3,4
1 2 9999
0 -4 1
3 1 0 2
-1 2 5 0
0 -2 2 1
1 -1 16 5
4 -10 -18 1
4,3,3,5
2 4 1
3 6 2
2 5 0
1 2 3
2 6 2 0 2
3 1 1 1 2
9999 2 2 0 1
20 18 10 4 13
32 28 16 6 20
19 17 9 5 14
20 14 10 2 9"""

lines = data.splitlines()

start = 1
m, r, r, n = [int(line) for line in lines[1].split(',')]
matrix_a = [[int(num) for num in line.split()] for line in lines[start + 1:start + 1 + m]]
matrix_b = [[int(num) for num in line.split()] for line in lines[start + 1 + m:start + 1 + m + r]]
matrix_c = [[int(num) for num in line.split()] for line in lines[start + 1 + m + r:start + 1 + 2 * m + r]]
for i in range(3):
  if max([row.count(9999) for row in [matrix_a, matrix_b, matrix_c][i]]) == 1: unknown = i
print(unknown)

if unknown == 0: matrix = (np.array(matrix_c).dot(np.linalg.inv(np.array(matrix_b))) - np.array(matrix_a)).tolist()
elif unknown == 1: matrix = (np.linalg.inv(np.array(matrix_a)).dot(np.array(matrix_c)) - np.array(matrix_b)).tolist()
else: matrix = (np.array(matrix_a).dot(np.array(matrix_b)) - np.array(matrix_c)).tolist()
print(matrix)


