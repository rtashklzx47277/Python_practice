import sys
data = sys.stdin.read()

roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
for line in data.splitlines()[1:]:
  reverse = line[::-1]
  ans = roman[reverse[0]]
  for i in range(1, len(reverse)):
    if roman[reverse[i]] < roman[reverse[i - 1]]: ans -= roman[reverse[i]]
    else: ans += roman[reverse[i]]
  print(ans)