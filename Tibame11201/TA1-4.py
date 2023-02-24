input = input().split(',')
player = input[0].split()
answer = input[1].split()

hit = 0
for i in player:
  if i in answer: hit += 1

if hit == 3: print(100)
elif hit == 4: print(1000)
elif hit == 5: print(10000)
else: print(0)