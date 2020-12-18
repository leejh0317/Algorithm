# 중복 있는 순열 / 각 집단에서 추출
from itertools import product as pd

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

result = list(pd(num, repeat=m))

for x in result:
    print(*x)
