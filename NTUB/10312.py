import sys
input = sys.stdin.read()

for line in input.splitlines()[1:]:
  given = line.split(',')
  a, b, c, d = int(given[0]), int(given[1]), int(given[2]), int(given[3])
  x = int((d - a * c) / (b - c))
  y = a - x
  print(f'{x},{y}')