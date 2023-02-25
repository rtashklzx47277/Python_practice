import sys, itertools
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  i, j, k = line.split(',')
  permutations = list(itertools.permutations(list(i)))
  s = sorted([int(''.join(permutation)) for permutation in permutations])
  num1, num2 = str(s[int(j) - 1]), str(s[int(k) - 1])
  
  length = len(list(i))
  count = 0
  for i in range(length):
    if num1[i] == num2[i]: count += 1
  print(f'{count}A{length - count}B')