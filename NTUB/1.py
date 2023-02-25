import sys
data = sys.stdin.read()

for line in data.splitlines():
  ans = count = 0
  for i in range(len(line) - 1):
    if line[i] <= line[i + 1]:
      count += 1
      if ans < count: ans = count
    else: count = 0
  print(ans + 1)