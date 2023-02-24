import sys
data = sys.stdin.read()

lines = data.splitlines()
ans = lines[1].split(',')

for line in lines[2:]:
  hit = {2: 0, 3: 0, 4: 0, 5: 0}
  for i in range(6):
    count = 0
    select = line.split(',')
    select.pop(i)
    for num in ans:
      if num in select: count += 1
    if count > 1: hit[count] += 1
  print(f'{hit[2]},{hit[3]},{hit[4]},{hit[5]}')