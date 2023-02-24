import random

start, end = 1, 100
ans = random.randrange(1, 100)

while True:
  try:
    num = int(input())
    if num < start or num > end: print('請輸入範圍內整數!')
    elif num == ans:
      print('正確答案!')
      break
    elif num > ans:
      end = num
      print(f'{start}~{end}')
    else:
      start = num
      print(f'{start}~{end}')
  except: print('請輸入範圍內整數!')