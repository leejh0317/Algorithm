import sys
input = lambda : sys.stdin.readline().rstrip()

a = int(input())

b = [int(input()) for i in range(a)]
b.sort()

for j in b:
    print(j)