# 1096 : [기초-2차원배열] 바둑판에 흰 돌 놓기(설명)
plate = [[0] * 19 for _ in range(19)]
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    plate[x-1][y-1] = 1

i = 0

while i < len(plate):
    print(*plate[i])
    i += 1