import sys
input = lambda : sys.stdin.readline().rstrip()

cnt = int(input())

for i in range(cnt):
    a, b = map(int, input().split())
    print(a+b)