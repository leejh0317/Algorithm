import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
dq = deque()

for _ in range(n):
    cmd, *num = input().split()

    if( cmd == "push_front" ):
        dq.appendleft(int(num[0]))
    elif( cmd == "push_back" ):
        dq.append(int(num[0]))
    elif( cmd == "pop_front" ):
        print(dq.popleft() if len(dq) > 0 else -1)
    elif( cmd == "pop_back" ):
        print(dq.pop() if len(dq) > 0 else -1)
    elif( cmd == "size" ):
        print(len(dq))
    elif( cmd == "empty" ):
        print(1 if len(dq) == 0 else 0)
    elif( cmd == "front" ):
        print(dq[0] if len(dq) > 0 else -1)
    elif( cmd == "back" ):
        print(dq[-1] if len(dq) > 0 else -1)