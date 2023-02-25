import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  num = int(line)
  temp = num
  ans = 'F'
  for i in range(100):
    num = sum([int(digit) ** 2 for digit in list(str(num))])
    if num == 1:
      ans = 'T'
      break
  print(ans)