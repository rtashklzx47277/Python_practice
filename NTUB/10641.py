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

for line in data.splitlines()[1:]:
  edges = [item.split(',') for item in line.split()]

  loop = None
  nodes_set = [[], [], [], [], [], [], [], [], [], []]
  for edge in edges:
    for nodes in nodes_set:
      if edge[0] in nodes and edge[1] in nodes: loop = (edge[0], edge[1])
      elif edge[0] in nodes or edge[1] in nodes:
        if edge[0] not in nodes: nodes.append(edge[0])
        if edge[1] not in nodes: nodes.append(edge[1])
        break
      elif not nodes:
        nodes.append(edge[0])
        nodes.append(edge[1])
        break
  temp = 0
  for i in range(10):
    if nodes_set[i] == []:
      temp = i
      break
  nodes_set = nodes_set[:temp]

  # nodes_new = []
  # for i in range(len(nodes_set) - 1):
  #   for j in range(i, len(nodes_set)):
  #     section = set(nodes_set[i]) & set(nodes_set[j])
  #     if section: nodes_new.append(nodes_set[i] + nodes_set[j])
  #     else:
  #       nodes_new.append(nodes_set[i])
  #       nodes_new.append(nodes_set[j])

  if loop: print('L')
  elif len(nodes_set) == 1: print('T')
  else: print('F')