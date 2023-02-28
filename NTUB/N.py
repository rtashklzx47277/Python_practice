import sys
# data = sys.stdin.read()

data = '''6
1 2 4 6
2 1 3 5
3 2 4
4 1 3
5 2 6
6 5 1
0
5
5 1 2 3 4
0
6
2 1 3
5 4 6 2
0
5
1 2
2 3
3 4
4 5
5 1
0
5
1 2
2 3
3 4
4 5
0
9
1 3 6
2 7 9
3 5 7 9
4 7
5 6 9
7 8
0
0'''

lines = data.splitlines()
graphs = []
for i in range(lines.count('0') - 1):
  graphs.append(lines[:lines.index('0')])
  del lines[:lines.index('0') + 1]

for graph in graphs:
  graph = [num.split() for num in graph]
  nums = []
  for map in graph:
    nums.append([int(num) for num in map])

  print(nums)