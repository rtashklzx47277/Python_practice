import sys
data = sys.stdin.read()

year = int(data) + 1911

if year % 4 != 0: print('False')
elif year % 100 != 0: print('True')
elif year % 400 != 0: print('False')
else: print('True')