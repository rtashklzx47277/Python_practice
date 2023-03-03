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

def dfs(visited, node):
  visited[node - 1] = True
  count = 1
  for neighbor in graph[node]:
    if not visited[neighbor - 1]: count += dfs(visited, neighbor)
  return count

lines = data.splitlines()
times = int(lines[0])
end = 1
for i in range(times):
  start = end
  nums = int(lines[start])
  end = start + nums + 1

  graph = {}
  for i in range(nums):
    graph.update({i + 1: []})

  for line in lines[start + 1:end]:
    u, v = [int(num) for num in line.split()]
    graph[u].append(v)
  
  start, count = 1, 0
  for node in graph:
    visit = [None for _ in range(nums)]
    temp = dfs(visit, node)
    if count < temp:
      count = temp
      start = node
    elif count == temp and start > node: start = node 
  print(start)