# 1080 : [기초-종합] 언제까지 더해야 할까?
n = int(input())
ans = 0

for x in range(1, n+1):
    ans += x

    if ans >= n:
        print(x)
        break