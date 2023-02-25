import sys
data = sys.stdin.read()

lines = data.splitlines()
for i in range(1, len(lines), 3):
  if lines[i] == '111' or lines[i + 1] == '111' or lines[i + 2] == '111': ans = 1
  elif lines[i] == '222' or lines[i + 1] == '222' or lines[i + 2] == '222': ans = 2
  elif lines[i][0] == lines[i + 1][0] == lines[i + 2][0]: ans = lines[i][0]
  elif lines[i][1] == lines[i + 1][1] == lines[i + 2][1]: ans = lines[i][1]
  elif lines[i][2] == lines[i + 1][2] == lines[i + 2][2]: ans = lines[i][2]
  elif lines[i][0] == lines[i + 1][1] == lines[i + 2][2]: ans = lines[i][0]
  elif lines[i][2] == lines[i + 1][1] == lines[i + 2][0]: ans = lines[i][2]
  else: ans = '3'
  if ans == '0': ans = '3'
  print(ans)