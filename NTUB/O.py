import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  nums = [int(num) for num in line.split()]
  if nums[0] < nums[1]: print('<')
  elif nums[0] > nums[1]: print('>')
  else: print('=')