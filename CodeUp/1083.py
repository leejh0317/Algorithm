# 1083 : [기초-종합] 3 6 9 게임의 왕이 되자!(설명)
n = int(input())

for x in range(1, n+1):
    if str(x).find('3') != -1 or str(x).find('6') != -1 or str(x).find('9') != -1:
        print('X', end=' ')
    else:
        print(x, end=' ')