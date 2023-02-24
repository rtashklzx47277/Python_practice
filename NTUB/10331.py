import sys
data = sys.stdin.read()

for line in data.splitlines()[1:]:
  score, amount = 0, []
  cards = sorted([int(card) for card in line.split()])
  if cards[4] - cards[0] == 4 and (cards[4] - 1) // 13 == (cards[0] - 1) // 13: score = 7
  elif cards[5] - cards[1] == 4 and (cards[5] - 1) // 13 == (cards[1] - 1) // 13: score = 7
  elif 1 in cards and 10 in cards and 11 in cards and 12 in cards and 13 in cards: score = 7
  elif 14 in cards and 23 in cards and 24 in cards and 25 in cards and 26 in cards: score = 7
  elif 27 in cards and 46 in cards and 47 in cards and 38 in cards and 39 in cards: score = 7
  elif 40 in cards and 49 in cards and 50 in cards and 51 in cards and 52 in cards: score = 7
  else:
    card_point = sorted([card % 13 for card in cards])
    for point in set(card_point): amount.append(card_point.count(point))
    amount.sort(reverse = True)
    if amount[0] == 4: score = 6
    elif amount[0] == 3 and amount[1] == 2: score = 5
    elif amount[0] == 3: score = 3
    elif amount[0] == 2 and amount[1] == 2: score = 2
    elif amount[0] == 2:
      card_five = sorted(list(set(card_point)))
      if card_five == [0, 9, 10, 11, 12] or card_five == [0, 1, 10, 11, 12] or card_five[4] - card_five[0] == 4: score = 4
      else: score = 1
    elif amount[0] == 1:
      if 0 in card_point and 1 in card_point and 10 in card_point and 11 in card_point and 12 in card_point: score = 4
      elif 0 in card_point and 9 in card_point and 10 in card_point and 11 in card_point and 12 in card_point: score = 4
      elif card_point[4] - card_point[0] == 4 or card_point[4] - card_point[0] == 4: score = 4
  print(score)