import sys
data = sys.stdin.read()

class BinaySearchTree():
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, node):
    while node:
      if node < self.value and self.left: self = self.left
      elif node > self.value and self.right: self = self.right
      else:
        if node < self.value: self.left = BinaySearchTree(node)
        else: self.right = BinaySearchTree(node)
        return

  def travel(self, root):
    post_travel = []
    if root:
      post_travel += self.travel(root.left)
      post_travel += self.travel(root.right)
      post_travel.append(root.value)
    return post_travel

for line in data.splitlines()[2::2]:
  nodes = [int(node) for node in line.split(',')]
  root = BinaySearchTree(nodes[0])
  for node in nodes[1:]: root.insert(node)
  print(*root.travel(root), sep = ',')