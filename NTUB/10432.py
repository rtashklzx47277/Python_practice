import sys
data = sys.stdin.read()

lines = data.splitlines()
times = int(lines[0])
end = 1
for i in range(times):
  start = end
  m, r, r, n = [int(num) for num in lines[start].split(',')]
  end = start + 2 * m + r + 1
  nums = []
  for line in lines[start + 1:end]:
    nums.append([int(num) for num in line.split()])
  for i in range(len(nums)):
    if 9999 in nums[i]: target = (i, nums[i].index(9999))
  matrix_a = nums[0:m]
  matrix_b = nums[m:m + r]
  matrix_c = nums[m + r:]

  if target[0] < m:
    for i in range(len(matrix_b[0])):
      if matrix_b[i][target[1]] == 0: continue
      else:
        temp = matrix_c[target[0]][i]
        for j in range(r):
          if j != target[1]: temp -= matrix_a[target[0]][j] * matrix_b[j][i]
        ans = temp // matrix_b[target[1]][i]
        break
  elif target[0] < m + r:
    for i in range(len(matrix_a)):
      if matrix_a[i][target[0] - m] == 0: continue
      else:
        temp = matrix_c[i][target[1]]
        for j in range(r):
          if j != target[0] - m: temp -= matrix_a[i][j] * matrix_b[j][target[1]]
        ans = temp // matrix_a[i][target[0] - m]
        break
  else:
    ans = 0
    for i in range(r): ans += matrix_a[target[0] - m - r][i] * matrix_b[i][target[1]]
  print(ans)