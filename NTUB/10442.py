import sys
data = sys.stdin.read()

def find_node(node):
  if tree[node] != node: tree[node] = find_node(tree[node])
  return tree[node]

for line in data.splitlines()[1:]:
  edges = [item.split(',') for item in line.split()]
  edges.sort(key = lambda edge: int(edge[2]))
  
  tree = {}
  for i, j, k in edges:
    if i not in tree: tree[i] = i
    if j not in tree: tree[j] = j

  ans = 0
  n = len(tree) - 1
  for edge in edges:
    node_a, node_b, weight = edge
    if find_node(node_a) != find_node(node_b):
      tree[find_node(node_b)] = find_node(node_a)
      ans += int(weight)
      n -= 1
      if n == 0: break
  print(ans)