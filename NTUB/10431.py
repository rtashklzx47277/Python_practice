import sys
data = sys.stdin.read()

for num in data.splitlines()[1:]:
  print(bin(int(num)).count('1'))