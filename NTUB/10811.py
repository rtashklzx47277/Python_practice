import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  point = []
  for mark in line:
    if mark == 'X': point.append(0)
    elif not point: point.append(1)
    else: point.append(point[-1] + 1)
  print(sum(point))