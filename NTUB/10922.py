import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  num = int(line)
  ans, i = '', 9
  while i > 1:
    if num % i == 0:
      num /= i
      ans += str(i)
    else: i -= 1
  if num == 1 and ans: print(ans[::-1])
  else: print(-1)