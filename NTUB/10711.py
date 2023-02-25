import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  ans = 0
  words = line.split()
  for word in words:
    if 's' in word or 'S' in word: ans += 1
  print(f'{len(words)},{ans}')