import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  print(len(line.split()))