import sys
data = sys.stdin.read()

def knapSack(W, n):
  if W == 0 or n == 0: return 0
  elif W < length[n - 1]: return knapSack(W, n - 1)
  else: return max(price[n - 1] + knapSack(W - length[n - 1], n - 1), knapSack(W, n - 1))

for line in data.splitlines():
  nums = [int(num) for num in line.split()]
  total = nums[0]
  length = price = nums[2:]
  print(knapSack(total, len(price)))