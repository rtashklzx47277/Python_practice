import sys
data = sys.stdin.read()

def knapSack(W, n):
  if W == 0 or n == 0: return 0
  elif W < length[n - 1]: return knapSack(W, n - 1)
  else: return max(price[n - 1] + knapSack(W - length[n - 1], n), knapSack(W, n - 1))

length = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
price = [1, 5, 8, 9, 10, 12, 17, 20, 24, 25]
for line in data.splitlines():
  total = int(line)
  print(knapSack(total, len(price)))