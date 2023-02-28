import sys
data = sys.stdin.read()

lines = data.splitlines()
times = int(lines[0])
end = 1
for i in range(times):
  start = end
  nodes, edges = int(lines[start]), int(lines[start + 1])
  end = start + edges + 2

  nums = []
  for line in lines[start + 2:end]:
    nums.append([int(num) for num in line.split()])

  dict = {}
  for i in range(nodes):
    dict.update({i: None})

  color = 'T'
  for edge in nums:
    if not dict[edge[0]] and not dict[edge[1]]:
      dict[edge[0]] = 'Water'
      dict[edge[1]] = 'Pink'
    elif not dict[edge[0]]:
      if dict[edge[1]] == 'Water': dict[edge[0]] = 'Pink'
      else: dict[edge[0]] = 'Water'
    elif not dict[edge[1]]:
      if dict[edge[0]] == 'Pink': dict[edge[1]] = 'Water'
      else: dict[edge[1]] = 'Pink'
    elif dict[edge[0]] != dict[edge[1]]: continue
    else:
      color = 'F'
      break
  print(color)