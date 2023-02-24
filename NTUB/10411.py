import sys
data = sys.stdin.read()

for line in data.splitlines()[2:][::2]:
  ans = 0
  floors = [int(floor) for floor in line.split(',')]
  for i in range(len(floors) - 1):
    d = floors[i+1] - floors[i]
    if d > 0: ans += d * 20
    else: ans -= d * 10
  print(ans)