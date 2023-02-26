import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  nums = [int(num) for num in line.split()]
  ans = -1310701
  for i in range(len(nums)):
    for j in range(i + 1, len(nums) + 1):
      if ans < sum(nums[i:j]): ans = sum(nums[i:j])
  print(ans)