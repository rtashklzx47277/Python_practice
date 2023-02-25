import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  nums = [int(num) for num in line.split()]
  if nums[0] == nums[2] and nums[1] == nums[3]: print(0)
  elif nums[0] == nums[2] or nums[1] == nums[3]: print(1)
  elif abs(nums[0] - nums[2]) == abs(nums[1] - nums[3]): print(1)
  else: print(2)