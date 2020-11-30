# 중복 없는 조합
from itertools import combinations as com
import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    k, *s = map(int, input().split())

    if k == 0:
        break

    lotto = list(com(s, 6))

    for x in lotto:
        print(*x)
    print()