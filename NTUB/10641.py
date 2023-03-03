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

class Graph:
  def __init__(self, edges, n):
    self.adj = {}
    for node in nodes: self.adj.update({node: []})

    for (a, b) in edges:
      self.adj[a].append(b)
      self.adj[b].append(a)
 
 
#函數對圖上的圖進行DFS遍歷
def DFS(graph, v, discovered, parent = -1):
 
    # 將當前節點標記為已發現
    discovered[v] = True
 
    # 對每條邊 (v, w) 執行
    for w in graph.adjList[v]:
 
        # 如果 `w` 沒有被發現
        if not discovered[w]:
            if DFS(graph, w, discovered, v):
                return True
 
        # 如果 `w` 被發現，並且 `w` 不是父母
        elif w != parent:
            # 我們發現了一個後沿(循環)
            return True
 
    # 圖中未發現後邊
    return False
 
 
# if __name__ == '__main__':
 
#     # 圖邊列表
#     edges = [
#         (0, 1), (0, 6), (0, 7), (1, 2), (1, 5), (2, 3),
#         (2, 4), (7, 8), (7, 11), (8, 9), (8, 10), (10, 11)
#         #邊(10, 11)在圖中引入了一個循環
#     ]
 
#     # 圖中節點總數(0到11)
#     n = 12
 
#     # 從給定的邊構建圖
#     graph = Graph(edges, n)
 
#     # 跟踪是否發現頂點
#     discovered = [False] * n
 
#     # 從第一個頂點開始進行DFS遍歷
#     if DFS(graph, 0, discovered):
#         print('The graph contains a cycle')
#     else:
#         print('The graph doesn\'t contain any cycle')

for line in data.splitlines()[1:]:
  edges, nodes = [], []
  for edge in line.split():
    a, b = (int(num) for num in edge.split(','))
    edges.append((a, b))
    if a not in nodes: nodes.append(a)
    if b not in nodes: nodes.append(b)
  graph = Graph(edges, len(nodes))
  print(graph.adj)
  break
