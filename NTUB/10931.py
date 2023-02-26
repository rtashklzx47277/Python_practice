import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  while True:
    if line == line[::-1]:
      ans = line
      break
    else:
      line = str(int(line) + int(line[::-1]))
  print(ans)