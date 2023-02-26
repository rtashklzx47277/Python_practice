import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  score, ans, num, end = line.split(), 0, 0, 0

  for i in range(len(score)):
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

    if score[i] == 'X': num += 2
    else: num += 1
    if num == 18:
      end = i + 1
      break

  if score[end] == 'X':
    ans += 10
    if score[end + 1] == 'X': ans += 10
    else: ans += int(score[end + 1])
    if score[end + 2] == 'X': ans += 10
    elif score[end + 2] == '/': ans += 10 - int(score[end + 1])
    else: ans += int(score[end + 2])
  elif score[end + 1] == '/':
    ans += 10
    if score[end + 2] == 'X': ans += 10
    else: ans += int(score[end + 2])
  else: ans += int(score[end]) + int(score[end + 1])
  print(ans)