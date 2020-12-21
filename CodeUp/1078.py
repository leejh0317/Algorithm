# 1078 : [기초-종합] 짝수 합 구하기(설명)
n = int(input())
ans = 0

for x in range(1, n+1):
    if(x % 2 == 0):
        ans += x

print(ans)