import sys
data = sys.stdin.read()

class Tree():
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def height(self):
    left, right = 0, 0
    if self.left: left =  1 + self.left.height()
    if self.right: right =  1 + self.right.height()
    return max(left, right, 1)

for line in data.splitlines()[1:]:
  nodes = [None if node == 'null' else int(node) for node in line[1:-1].split(',')]
  root = Tree(nodes[0])
  tree_nodes = [root]
  for i, value in enumerate(nodes[1:]):
    if value is None: continue
    parent = tree_nodes[i // 2]
    node = Tree(value)
    if i % 2 == 0: parent.left = node
    else: parent.right = node
    tree_nodes.append(node)

  ans = 0
  if root.left: ans += root.left.height()
  if root.right: ans += root.right.height()
  print(ans)