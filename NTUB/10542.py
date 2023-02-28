import sys
data = sys.stdin.read()

class Tree():
  def __init__(self, left, right):
    self.left = left
    self.right = right

def huffman(node, code = ''):
  if type(node) is int: return {node: code}
  dict = {}
  dict.update(huffman(node.left, code + '0'))
  dict.update(huffman(node.right, code + '1'))
  return dict

for line in data.splitlines()[1:]:
  nums = [(int(nums), int(nums)) for nums in line.split(',')]
  nums_sort = sorted(nums, reverse = True)
  while len(nums_sort) > 1:
    node_a, value_a = nums_sort[-1]
    node_b, value_b = nums_sort[-2]
    nums_sort = nums_sort[:-2]
    node = Tree(node_a, node_b)
    nums_sort.append((node, value_a + value_b))
    nums_sort = sorted(nums_sort, key = lambda node: node[1], reverse = True)
  
  ans = ''
  for node, value in nums:
    ans += f'{len(huffman(nums_sort[0][0])[node])},'
  print(ans[:-1])