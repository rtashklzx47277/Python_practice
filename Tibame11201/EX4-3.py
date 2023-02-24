input = int(input())

while input > 1:
  check = True
  for i in range(2, int(input ** 0.5) + 1):
    if input % i == 0:
      check = False
      break
  if check:
    print(input)
    break
  else: input -= 1