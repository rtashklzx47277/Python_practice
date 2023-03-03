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
  graph = [[] for _ in range(nums)]

  for j in range(nums):
    u, v = map(int, lines[start + 1:end][j].split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

  # edges = []
  # for line in lines[start + 1:end]:
  #   edges.append([int(num) for num in line.split()])
  # edges.sort(key = lambda node: node[0])

  # dict = {}
  # for i in range(nums): dict[i + 1] = set()

  # check = None
  # for i in range(nums):
  #   temp = edges[i][1]
  #   while temp != i + 1 and temp not in dict[i + 1]:
  #     dict[i + 1].add(temp)
  #     temp = edges[temp - 1][1]
  #   if len(dict[i + 1]) == nums - 1:
  #     check = i + 1
  #     break

  # if check: print(check)
  # else: print(max(dict, key = lambda node: len(dict[node])))

T = int(input())
for i in range(T):
    N = int(input())
    graph = [[] for _ in range(N)]
    for j in range(N):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    # 找到連通分量中最小度數的節點
    min_degree = sys.maxsize
    start_node = 0
    for j in range(N):
        if len(graph[j]) < min_degree:
            min_degree = len(graph[j])
            start_node = j
    
    # 將特殊郵件發送給 start_node，因為它有最小度數
    print(f"Case {i+1}: {start_node+1}")