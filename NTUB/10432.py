# import sys
# data = sys.stdin.read()
data = """2
2,3,3,4
1 2 9999
0 -4 1
3 1 0 2
-1 2 5 0
0 -2 2 1
1 -1 16 5
4 -10 -18 1
4,3,3,5
2 4 1
3 6 2
2 5 0
1 2 3
2 6 2 0 2
3 1 1 1 2
9999 2 2 0 1
20 18 10 4 13
32 28 16 6 20
19 17 9 5 14
20 14 10 2 9"""

lines = data.splitlines()

m, r, r, n = lines[1].split(',')
start, end = 2, 2 * int(m) + int(r) + 2
matrix1 = lines[start:end]
temp = [[]] * 3
print(temp)
for line in matrix1:
  line = line.split(',')
  temp[0].append
  print(line)

# lines = data.splitlines()
# num = int(lines[0])
# l = []
# for line in lines:
#   if ',' in line:
#     m, r, r, n = line.split(',')
#     l.append

# for line in data.splitlines()[1:]:
#   print(bin(int(num)).count('1'))