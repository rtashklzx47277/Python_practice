import sys
data = sys.stdin.read()

class Tree():
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, node):
    if self.left:
      self.right = Tree(node)
      return self.right
    else:
      self.left = Tree(node)
      return self.left

  def max_value(self):
    value = self.value
    if self.left:
      left_max = self.left.max_value()
      if value < left_max: value = left_max
    if self.right:
      right_max = self.right.max_value()
      if value < right_max: value = right_max
    return value
  
  def min_value(self):
    value = self.value
    if self.left:
      left_min = self.left.min_value()
      if value > left_min: value = left_min
    if self.right:
      right_min = self.right.min_value()
      if value > right_min: value = right_min
    return value

  def is_bst(self):
    if self.left:
      if self.value < self.left.max_value() or not self.left.is_bst(): return False
    if self.right:
      if self.value > self.right.min_value() or not self.right.is_bst(): return False
    return True

for line in data.splitlines()[1:]:
  nodes = [int(node) for node in line.split(',')]
  min_heap = True
  max_heap = True
  for i in range(1, len(nodes)):
    if nodes[i] < nodes[(i - 1) // 2]: min_heap = False
    else: max_heap = False

  if min_heap or max_heap: print('H')
  else:
    root = Tree(nodes[0])
    tree_nodes = [root]
    for i in range(1, len(nodes)):
      node = tree_nodes[(i - 1) // 2].insert(nodes[i])
      tree_nodes.append(node)
    bst = root.is_bst()
    if bst: print('B')
    else: print('F')