import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  nums = [int(num) for num in line[1:-1].split(',')]
  ans = []
  for i in range(len(nums)):
    check = False
    for list in ans:
      if i + 1 in list: check = True
    if not check:
      ans.append([i + 1])
      temp = nums[i]
      while i + 1 != temp:
        temp = nums[temp - 1]
        ans[-1].append(nums.index(temp) + 1)
  print(ans)