import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  ans = 0
  for i in range(6):
    select = line.split()
    select.pop(i)

    cards = []
    for card in select:
      point = int(card) % 13
      if point == 0: point = 13
      cards.append(point)
    cards.sort()
    count = sorted([cards.count(point) for point in set(cards)], reverse = True)
    
    if len(set([(int(card) - 1) // 13 for card in select])) == 1 and (cards == [1, 10, 11, 12, 13] or cards[4] - cards[0] == 4): score = 7
    elif count[0] == 4: score = 6
    elif count[0] == 3 and count[1] == 2: score = 5
    elif cards == [1, 10, 11, 12, 13] or cards[4] - cards[0] == 4: score = 4
    elif count[0] == 3: score = 3
    elif count[0] == 2 and count[1] == 2: score = 2
    elif count[0] == 2: score = 1
    else: score = 0
    if ans < score: ans = score
  print(ans)