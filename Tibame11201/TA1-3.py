input = input().split()
if input[0] in ['星期五', '星期六', '星期日']: print('不開市')
else: print(int(input[1]) * int(input[2]))