# 1081 : [기초-종합] 주사위를 2개 던지면?(설명)
n, m = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, j)