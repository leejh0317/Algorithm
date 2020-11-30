# 중복 없는 조합
from itertools import combinations as com
import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

arr = list(com(range(1, n+1), m))

for x in arr:
    print(*x)