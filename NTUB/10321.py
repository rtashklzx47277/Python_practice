import sys
lines = sys.stdin.read().splitlines()

for i in range(int(lines[0])):
  out = ''
  for j in range(ord('a'), ord('a') + 26):
    l = chr(j)
    if l in lines[2*i+1] and l in lines[2*i+2]: out += l
  if out: print(out)
  else: print('N')