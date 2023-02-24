# import sys
# data = sys.stdin.read()
data = """1 1 1 1
1 10 100 1000"""

fibonacci = [1, 1]
for line in data.splitlines():
  nums = [int(num) for num in line.split()]
  index = nums[0] * 56 + nums[1] * 24 + nums[2] * 14 + nums[3] * 6
  for i in range(index - 2): fibonacci.append(fibonacci[i] + fibonacci[i + 1])
  print(fibonacci[-5:])
