import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  edges = [item.split(',') for item in line.split()]
  edges_sort = sorted(edges, key = lambda edge: int(edge[2]))
  
  nodes, ans = [], 0
  for edge in edges_sort:
    if edge[0] in nodes and edge[1] in nodes: pass
    else:
      if edge[0] not in nodes: nodes.append(edge[0])
      if edge[1] not in nodes: nodes.append(edge[1])
      ans += int(edge[2])
  print(ans)