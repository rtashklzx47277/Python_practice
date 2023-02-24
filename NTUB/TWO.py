import sys
data = sys.stdin.read()

print(sum(int(num) for num in data.split()))