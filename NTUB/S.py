import sys
data = sys.stdin.read()

for line in data.splitlines()[2::2]:
  money = 0
  values = sorted([int(value) for value in line.split()], reverse = True)
  for i in range(2, len(values), 3):
    money += values[i]
  print(money)