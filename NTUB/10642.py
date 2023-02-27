import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  postfix = line.split()
  temp = []
  for i in postfix:
    if i == '+':
      temp.append(int(temp[-2]) + int(temp[-1]))
      del temp[-3:-1]
    elif i == '-':
      temp.append(int(temp[-2]) - int(temp[-1]))
      del temp[-3:-1]
    elif i == '*':
      temp.append(int(temp[-2]) * int(temp[-1]))
      del temp[-3:-1]
    elif i == '/':
      temp.append(int(temp[-2]) // int(temp[-1]))
      del temp[-3:-1]
    else: temp.append(i)
  print(temp[0])