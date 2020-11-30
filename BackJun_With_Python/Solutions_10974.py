# 중복 없는 순열
from itertools import permutations as pm

n = int(input())
arr = list(pm(range(1, n+1), n))

for x in arr:
    # Unpacking => *x
    print(*x)