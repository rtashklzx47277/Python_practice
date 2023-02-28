import sys
# data = sys.stdin.read()

data = '''9
5,8 5,3 5,2 5,4 5,6 1,2 2,0
8,1 1,3 6,2 8,10 7,5 1,4 7,8 8,6 8,0
3,8 6,8 6,4 0,6 8,2 2,0 5,3
1,0 4,3 1,2
1,2 2,3 4,0
4,3 2,3 2,1 1,0
1,2 2,3 3,4 1,4 1,5
1,2 1,3 2,3
1,2 2,3 3,4 1,5 5,4'''

def find_node(node):
  if tree[node] != node: tree[node] = find_node(tree[node])
  return tree[node]

for line in data.splitlines()[1:]:
  edges = [item.split(',') for item in line.split()]
  
  tree = {}
  for i, j in edges:
    if i not in tree: tree[i] = i
    if j not in tree: tree[j] = j

  n = len(tree) - 1
  span = []
  for edge in edges:
    node_a, node_b = edge
    if find_node(node_a) != find_node(node_b):
      tree[find_node(node_b)] = find_node(node_a)
      span.append(edge)
      n -= 1
      if n == 0: break
  print(span)