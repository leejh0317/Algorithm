# 1098 : [기초-2차원배열] 설탕과자 뽑기
r, c = map(int, input().split())
board = [[0] * c for j in range(r)]

i = 0

n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())

    for j in range(l):
        if d == 0:
            board[x-1][y-1+j] = 1
        elif d == 1:
            board[x-1+j][y-1] = 1

i = 0

while i < len(board):
    print(*board[i])
    i+=1