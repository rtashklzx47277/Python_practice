import sys
data = sys.stdin.read()

morse = {'-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'}
for line in data.splitlines()[1:]:
  ans = ''
  for single in line.split():
    ans += morse[single]
  print(ans)