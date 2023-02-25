import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  num1, num2 = [int(num) for num in line.split(',')]
  print(len(list(str(num1 ** num2))))