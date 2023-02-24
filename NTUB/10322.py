import sys
lines = sys.stdin.read().splitlines()

for i in range(int(lines[0])):
  count = 0
  list1 = lines[2 * i + 1].split()
  list2 = lines[2 * i + 2].split()
  if int(list1[0]) < int(list2[0]):
    for j in list1[1:]:
      if j in list2[1:]: count += 1
  else:
    for k in list2[1:]:
      if k in list1[1:]: count += 1
  print(count)