input = input().split()

for i in range(len(input)): input[i] = str(int(input[i]) + 1)
print(' '.join(input))