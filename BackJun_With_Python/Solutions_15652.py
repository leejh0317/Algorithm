# 중복 있는 조합
from itertools import combinations_with_replacement as com

n, m = map(int, input().split())
arr = list(com(range(1, n+1), m))

for x in arr:
    print(*x)