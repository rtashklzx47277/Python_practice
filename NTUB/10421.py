import sys, itertools
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  i, j, k = line.split(',')
  permutations = list(itertools.permutations(list(i)))
  s = sorted([int(''.join(permutation)) for permutation in permutations])
  print(s[int(j) - 1] + s[int(k) - 1])