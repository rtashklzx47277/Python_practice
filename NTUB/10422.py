import sys, math
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  numbers = [int(line) for line in line.split(',')]
  ans = math.gcd(numbers[0], numbers[1])
  for i in range(1, len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
      if ans > math.gcd(numbers[i], numbers[i + 1]):
        ans = math.gcd(numbers[i], numbers[i + 1])
  print(ans)