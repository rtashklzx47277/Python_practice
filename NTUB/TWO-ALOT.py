import sys
data = sys.stdin.read()

for line in data.splitlines():
  print(sum(int(num) for num in line.split()))