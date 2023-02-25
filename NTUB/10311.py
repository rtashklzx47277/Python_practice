import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  check = 'Y'
  num1 = int(line.split(',')[0])
  num2 = int(line.split(',')[1])

  if num2 - num1 == 2:
    for i in range(2, int(num1 ** 0.5) + 1):
      if num1 % i == 0: check = 'N'
    for j in range(2, int(num2 ** 0.5) + 1):
      if num2 % j == 0: check = 'N'
  else: check = 'N'
  print(check)