import sys, math
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  ans = 0
  nums = [int(num) for num in line.split(',')]
  for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
      temp = math.gcd(nums[i], nums[j])
      if ans < temp: ans = temp
  print(ans)