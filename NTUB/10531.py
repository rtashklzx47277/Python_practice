import sys
# data = sys.stdin.read()

# data = '''3
# 4,8,6,1,10,16,5,14,13
# 1,4,5,6,8,10,13,14,16
# 4,8,6,10
# 16,14,13,4,8,6,5,10,1
# 16,14,10,13,4,6,5,1,8
# 7,4,12,1,5,8,10
# 9,6,12,2,8,11,15,1,3,7'''

data = '''1
1,4,5,6,8,10,13,14,16'''
class Tree():
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, node):
    if node < self.value and self.left: self.left.insert(node)
    elif node > self.value and self.right: self.right.insert(node)
    elif node < self.value: self.left = Tree(node)
    else: self.right = Tree(node)

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
  # print(min_heap, max_heap)

  root = Tree(nodes[0])
  for node in nodes[1:]: root.insert(node)
  print(root.left.node)
  root.is_bst()
