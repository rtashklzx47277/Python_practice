import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  a = b = ''
  for digit in line:
    if digit != '4':
      a += digit
      b += '0'
    else:
      a += '3'
      b += '1'
  print(int(a), int(b))