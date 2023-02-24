import sys
data = sys.stdin.read()

for line in data.splitlines():
  fibonacci = [1, 1]
  nums = [int(num) for num in line.split()]
  index = nums[0] * 56 + nums[1] * 24 + nums[2] * 14 + nums[3] * 6
  for i in range(index - 2):
    fibonacci.append(fibonacci[0] + fibonacci[1])
    fibonacci.pop(0)
  print(fibonacci[1])