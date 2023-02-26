import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  a, b = [int(num) for num in line.split()]

  remainder = a % b
  if remainder == 0: print(f'{a // b}.(0)')
  else:
    remainders = [remainder]
    nums, infinite = [], True

    while True:
      digit = remainder * 10 // b
      remainder = remainder * 10 % b
      nums.append(digit)
      if remainder == 0:
        infinite = False
        break
      elif remainder in remainders: break
      else: remainders.append(remainder)

    if infinite:
      index = remainders.index(remainder)
      c = ''.join([str(num) for num in nums[:index]])
      d = ''.join([str(num) for num in nums[index:]])
      if len(d) > 50: d = d[:50] + '...'
      print(f'{a // b}.{c}({d})')
    else:
      c = ''.join([str(num) for num in nums])
      if len(c) > 50: c = c[:50] + '...'
      print(f'{a // b}.{c}(0)')