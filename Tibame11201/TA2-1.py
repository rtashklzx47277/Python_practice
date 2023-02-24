input = input().split()

i = 1
while i <= int(input[0]):
  j = 1
  while j <= int(input[1]):
    print(f'{i}x{j}={i * j}')
    j += 1
  i += 1