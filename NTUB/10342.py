import sys
data = sys.stdin.read()

lines = data.splitlines()
times = int(lines[0])
end = 1
for i in range(times):
  start = end
  row, tree, target = [int(num) for num in lines[start].split(',')]
  end = start + row + 1

  nums = []
  for line in lines[start + 1:end]:
    nums.append([int(num) for num in line.split()])

  for i in range(len(nums)):
    if 999 in nums[i]: root = i

  ans = []
  for i in range(tree):
    length = 1
    temp = nums[target][i + 1]
    while temp != root:
      length += 1
      temp = nums[temp][i + 1]
    ans.append(length)
  print(*ans, sep = ',')