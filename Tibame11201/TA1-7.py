input = input()
if '+' in input:
  num = input.split('+')
  print(int(num[0]) + int(num[1]))
elif '-' in input:
  num = input.split('-')
  print(int(num[0]) - int(num[1]))
elif '*' in input:
  num = input.split('*')
  print(int(num[0]) * int(num[1]))
else:
  num = input.split('/')
  print(int(int(num[0]) / int(num[1])))