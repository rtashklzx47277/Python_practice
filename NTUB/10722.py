import sys, itertools
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  nums = line.split(',')
  permutations = list(itertools.permutations(list(nums[1:-1])))
  s = sorted([int(''.join(permutation)) for permutation in permutations])
  ans = s[int(nums[-1]) - 1]
  if '0' in nums[1:-1] and '0' not in str(ans): ans = '0' + str(ans)
  print(ans)