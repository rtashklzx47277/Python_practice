import sys
from datetime import datetime
data = sys.stdin.read()

lines = data.splitlines()[1:]
for i in range(0, len(lines), 2):
  now = datetime.strptime(lines[i], '%d/%m/%Y')
  birth = datetime.strptime(lines[i + 1], '%d/%m/%Y')
  ans = now.year - birth.year
  if now.month - birth.month < 0: ans -= 1
  elif now.month - birth.month == 0 and now.day - birth.day < 0: ans -= 1
  print(ans)