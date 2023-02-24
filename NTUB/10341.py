import sys
data = sys.stdin.read()

digit = ['111101', '111100', '11101', '11100', '1101', '1100', '101', '100', '01', '00']
for line in data.splitlines()[1:]:
  ans = ''
  while line:
    for i in range(10):
      if digit[i] in line and line.index(digit[i]) == 0:
        ans += str(9 - i)
        line = line[len(digit[i]):]
  if int(ans) > 23: print(chr(ord('A') + int(ans) - 24))
  else: print(chr(ord('D') + int(ans) - 1))