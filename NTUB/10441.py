import sys
data = sys.stdin.read()

class BinaySearchTree():
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, node):
    if node < self.value and self.left: self.left.insert(node)
    elif node > self.value and self.right: self.right.insert(node)
    elif node < self.value: self.left = BinaySearchTree(node)
    else: self.right = BinaySearchTree(node)

  def post_travel(self):
    post_order = []
    if self.left: post_order += self.left.post_travel()
    if self.right: post_order += self.right.post_travel()
    post_order.append(self.value)
    return post_order

for line in data.splitlines()[2::2]:
  nodes = [int(node) for node in line.split(',')]
  root = BinaySearchTree(nodes[0])
  for node in nodes[1:]: root.insert(node)
  print(*root.post_travel(), sep = ',')