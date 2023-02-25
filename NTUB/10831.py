import sys
data = sys.stdin.read()

lines = data.splitlines()
times = int(lines[0])
end = 1
for i in range(times):
  start = end
  row, column = [int(num) for num in lines[start].split()]
  end = start + row + 1
  dna = [list(line) for line in lines[start + 1:end]]
  dna_transpose = [[dna[j][i] for j in range(row)] for i in range(column)]
  ans = []
  for row in dna_transpose:
    value = 0
    if row.count('A') > value:
      value = row.count('A')
      temp = 'A'
    if row.count('C') > value:
      value = row.count('C')
      temp = 'C'
    if row.count('G') > value:
      value = row.count('G')
      temp = 'G'
    if row.count('T') > value:
      value = row.count('T')
      temp = 'T'
    ans.append(temp)
  print(''.join(ans))