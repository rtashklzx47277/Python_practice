import sys
data = sys.stdin.read()

fibonacci = [1, 2]
for i in range(15): fibonacci.append(fibonacci[i] + fibonacci[i + 1])
fibonacci.sort(reverse = True)

data_list = [int(num) for num in data.splitlines()[1:]]
for data in data_list:
  ans = '0'
  for i in range(17):
    if ans[-1] == '1': ans += '0'
    elif data >= fibonacci[i]:
      ans += '1'
      data -= fibonacci[i]
    else: ans += '0'

  print(int(ans))