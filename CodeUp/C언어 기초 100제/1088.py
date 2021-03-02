# 1088 : [기초-종합] 3의 배수는 통과?(설명)
n = int(input())

for x in range(1, n+1):
    if x%3 == 0:
        continue
    print(x, end=' ')