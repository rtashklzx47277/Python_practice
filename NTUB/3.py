import sys
data = sys.stdin.read()

data_list = [int(num) for num in data.split(',')]
m, n = data_list[0], data_list[1]
matrix = []
for i in range(m):
  matrix.append(data_list[2 + n * i:2 + n * i + n])
ans = []
for i in range(m - 2):
  for j in range(n - 2):
    ans.append(matrix[i][j] - matrix[i][j + 1] + matrix[i][j + 2] - matrix[i + 1][j] + matrix[i + 1][j + 1] - matrix[i + 1][j + 2] + matrix[i + 2][j] - matrix[i + 2][j + 1] + matrix[i + 2][j + 2])
print(max(ans))