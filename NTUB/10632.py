import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  nums = [int(num) for num in line.split(',')]
  nums_sort = sorted(nums)
  ans = [nums_sort.index(i) + 1 for i in nums]
  print(*ans, sep = ', ')