class BinaySearchTree():
  def __init__(self, value: int) -> None:
    self.val = value
    self.left = None
    self.right = None

nodes = [7,4,1,5,12,8,9,15]
root = BinaySearchTree(7)

i = 1
while i < len(nodes):
  if i == 1 or i > pointer:
    pointer = i
    node = root
  
  if nodes[i] < node.val and node.left:
    node = node.left
    continue
  elif nodes[i] < node.val:
    node.left = BinaySearchTree(nodes[i])
    i += 1
  elif nodes[i] > node.val and node.right:
    node = node.right
    continue
  elif nodes[i] > node.val:
    node.right = BinaySearchTree(nodes[i])
    i += 1

travel = []
while True:
  if node.left:
    node = node.left
  else:
    node = node.right
  

print(root.right.left.right.val)