import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  a, b, n = [int(num) for num in line.split()]
  ans = 0
  for num in range(a, b + 1):
    if str(n) in str(num): ans += 1
  print(ans)