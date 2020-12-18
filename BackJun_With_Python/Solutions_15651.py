# 중복 있는 순열 / 각 집단에서 추출
from itertools import product

n, m = map(int, input().split())
arr = list(product(range(1, n+1), repeat = m))

for x in arr:
    print(*x)
