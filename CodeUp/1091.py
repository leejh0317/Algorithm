# 1091 : [기초-종합] 수 나열하기3
a, m, d, n = map(int, input().split())
ans = a

for x in range(1, n):
    ans = ans * m + d
print(ans)