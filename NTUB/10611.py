import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  ans = 0
  for word in line.split():
    if 's' in word or 'S' in word: ans += 1
  print(ans)