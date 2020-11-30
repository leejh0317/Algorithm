# 중복 없는 순열
from itertools import permutations as pm
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
p = list(pm(arr))

v = 0

for x in p:
    total = 0

    for i in range(n-1):
        total += abs(x[i]-x[i+1])
    
    v = max(v, total)

print(v)