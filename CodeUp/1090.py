# 1090 : [기초-종합] 수 나열하기2
a, r, n = map(int, input().split())
ans = a

for _ in range(1, n):
    ans = ans * r

print(ans)