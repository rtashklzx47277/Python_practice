import sys
data = sys.stdin.read()

for line in data.splitlines():
  ans = ''
  for a in line[::-1]:
    if a not in ans: ans += a
  print(ans[::-1])