# 1073 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기2(설명)
n = map(int, input().split())

for x in n:
    if x == 0:
        break
    else:
        print(x)