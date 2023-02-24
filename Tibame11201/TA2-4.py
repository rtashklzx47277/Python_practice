import sys
input = sys.stdin.read()

i = 1
for line in input.splitlines():
  print(f'{line}{i}')
  i += 1
