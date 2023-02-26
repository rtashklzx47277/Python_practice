import sys
data = sys.stdin.read()

class Tree():
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def bulid(self, pre_order, in_order):
    if not pre_order or not in_order: return
    root = Tree(pre_order[0])
    index = in_order.index(pre_order[0])
    root.left = self.bulid(pre_order[1:1 + index], in_order[:index])
    root.right = self.bulid(pre_order[1 + index:], in_order[index + 1:])
    return root
  
  def post_travel(self):
    post_order = []
    if self.left: post_order += self.left.post_travel()
    if self.right: post_order += self.right.post_travel()
    post_order.append(self.value)
    return post_order

lines = data.splitlines()
for i in range(1, len(lines), 2):
  in_order = [int(node) for node in lines[i].split(',')]
  pre_order = [int(node) for node in lines[i + 1].split(',')]
  root = Tree(pre_order[0]).bulid(pre_order, in_order)
  print(*root.post_travel(), sep = ',')