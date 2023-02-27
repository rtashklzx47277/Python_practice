import sys
data = sys.stdin.read()

lines = data.splitlines()
for i in range(1, len(lines), 2):
  list_a = list(lines[i])
  list_b = list(lines[i + 1])
  temp = [[0] * (len(list_b) + 1)] * (len(list_a) + 1)
  for i in range(len(list_a)):
    for j in range(len(list_b)):
      if list_a[i] == list_b[j]: temp[i + 1][j + 1] = temp[i][j] + 1
      else: temp[i + 1][j + 1] = max(temp[i + 1][j], temp[i][j + 1])
  print(temp[-1][-1])