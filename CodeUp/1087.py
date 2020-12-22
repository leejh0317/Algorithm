# 1087 : [기초-종합] 여기까지! 이제 그만~(설명)
n = int(input())
ans = 0

for x in range(n+1):
    ans = ans+x

    if ans >= n:
        break
print(ans)