import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  nums = sorted([int(num) for num in line.split()])
  print(nums[-1], nums[-2])