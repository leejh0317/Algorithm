# 1097 : [기초-2차원배열] 바둑알 십자 뒤집기(설명)
m = 19
board =[[int(x) for x in input().split()]for y in range(m)]

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    
    for j in range(m):
        if board[j][y-1] == 0:
            board[j][y-1] = 1
        else:
            board[j][y-1] = 0

        if board[x-1][j] == 0:
            board[x-1][j] = 1
        else:
            board[x-1][j] = 0

i = 0

while i < len(board):
    print(*board[i])
    i += 1