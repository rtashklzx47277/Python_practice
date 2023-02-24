num = int(input())
n = 0

while num != 0:
  if num % 2 == 1: num -= 1
  else: num /= 2
  n += 1
print(n)