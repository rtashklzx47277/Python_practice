input = input()

output = ''
for item in input[::-1]:
  if item not in output: output += item
print(output[::-1])