year = int(input())

if year % 4 != 0: print(False)
elif year % 100 != 0: print(True)
elif year % 400 != 0: print(False)
else: print(True)