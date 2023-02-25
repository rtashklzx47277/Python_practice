import sys
data = sys.stdin.read()

def count(n, k):
  if n == 0: return 0
  elif k == 0: return 1
  else:
    sum = 0
    for i in range(n):
      if k - i >= 0: sum += count(n - 1, k - i)
    return sum

for line in data.splitlines()[1:]:
  nums = line.split()
  n = int(nums[0])
  k = int(nums[1])
  print(count(n, k))