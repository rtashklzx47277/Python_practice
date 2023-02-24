input = int(input())

list = [0, 1]
i = 2
while i < input:
  list.append(list[i-1] + list[i-2])
  i += 1
if input == 1: print(0)
else: print(list[-1])