# 1094 : [기초-1차원배열] 이상한 출석 번호 부르기2(설명)
n = int(input())
call = list(map(int, input().split()))

for i in range(1, n+1):
    if i != 0:
        print(call[-i], end = ' ')