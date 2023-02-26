# import sys
# data = sys.stdin.read()

data = '''10
1 0 1 / 2 2 X 3 3 X 1 / 3 / X 1 2
6 3 9 / X 8 0 X X 5 2 7 / 9 / X 3 4
1 0 1 / 2 2 X 3 3 X 1 / 3 / 1 / X 8 0
1 0 1 / 2 2 X 3 3 X 1 / 3 / 1 / 8 / 9
6 2 8 0 5 1 X 7 2 X 6 / 3 2 4 5 5 / 8
6 2 8 0 5 1 X 7 2 X 6 / 3 2 4 5 X X 8
X X X X X X X X X X X X
X 9 / X 7 / X 2 / X 5 / X 1 / X
9 / 8 / 6 / 7 / 7 / 9 / 5 / 8 / 9 / 9 / X
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'''

for line in data.splitlines()[1:]:
  score = line.split()
  ans, num, end = 0, 0, 0
  
  for i in range(len(score)):
    if score[i] == 'X': num += 2
    else: num += 1
    if num == 18: end = i + 1

  for i in range(end):
    if score[i] == 'X':
      ans += 10
      if score[i + 1] == 'X': ans += 10
      else: ans += int(score[i + 1])
      if score[i + 2] == 'X': ans += 10
      elif score[i + 2] == '/': ans += 10 - int(score[i + 1])
      else: ans += int(score[i + 2])
    elif score[i] == '/':
      ans += 10 - int(score[i - 1])
      if score[i + 1] == 'X': ans += 10
      else: ans += int(score[i + 1])
    else: ans += int(score[i])

  if score[end] == 'X':
    ans += 10
    if score[end + 1] == 'X': ans += 10
    else: ans += int(score[end + 1])
    if score[end + 2] == 'X': ans += 10
    else: ans += int(score[end + 2])
  elif score[end + 1] == '/':
    ans += 10
    if score[end + 2] == 'X': ans += 10
    else: ans += int(score[end + 2])
  else: ans += int(score[end]) + int(score[end + 1])
  print(ans)