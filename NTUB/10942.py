import sys
# data = sys.stdin.read()

data = '''8
3
1 2
2 3
3 1
4
1 2
2 1
4 3
3 2
5
1 2
2 1
5 3
3 4
4 5
6
1 2
2 3
3 4
4 5
5 1
6 3
6
2 3
3 4
4 5
5 6
6 2
1 4
7
1 2
2 3
3 4
4 5
5 1
6 3
7 6
7
2 3
3 4
4 5
5 6
6 2
7 4
1 7
7
5 4
3 4
4 6
6 7
7 1
1 2
2 1'''

lines = data.splitlines()
times = int(lines[0])
end = 1
for i in range(times):
  start = end
  nums = int(lines[start])
  end = start + nums + 1

  edges = []
  for line in lines[start + 1:end]:
    edges.append([int(num) for num in line.split()])
  edges.sort(key = lambda node: node[0])

  dict = {}
  for i in range(nums): dict.update({i + 1: [i + 1]})

  check = None
  for i in range(nums):
    temp = edges[i][1]
    for j in range(nums):
      if temp in dict[i + 1]: break
      dict[i + 1].append(temp)
      temp = edges[temp - 1][1]
    if len(dict[i + 1]) == nums:
      check = i + 1
      break

  if check: print(check)
  else:
    ans = (0, 0)
    for item in dict:
      if ans[1] < len(dict[item]): ans = (item ,len(dict[item]))
    print(ans[0])