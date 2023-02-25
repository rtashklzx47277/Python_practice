import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  nums = line.split('/')
  ip = [int(section) for section in nums[0].split('.')]
  subnet = [int(section) for section in nums[1].split('.')]
  print(*[ip[i] & subnet[i] for i in range(4)], sep = '.')