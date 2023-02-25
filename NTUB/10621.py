import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  new_new, new = [], []
  for i in range(16):
    if i % 2 == 0: new.append(str(int(line[i]) * 2))
    else: new.append(line[i])
  for j in range(16):
    num = 0
    if len(new[j]) > 1:
      for a in new[j]: num += int(a)
      new_new.append(num)
    else: new_new.append(int(new[j]))
  if sum(new_new) % 10 == 0: print('T')
  else: print('F')