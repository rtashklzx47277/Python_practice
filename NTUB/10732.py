import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  num = [int(num) for num in line.split()]
  ans = 0
  for i in range(num[0], num[1] + 1):
    for j in range(num[2], num[3] + 1):
      for k in range(num[4], num[5] + 1):
        if (i + j) % k == (i - j) % k: ans += 1
  print(ans)