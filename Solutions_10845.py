import sys
import queue
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
q = queue.Queue()

for _ in range(n):
    cmd, *num = input().split()

    if(cmd == "push"):
        q.put(num[0])
    elif(cmd == "pop"):
        print(q.get() if not q.empty() else -1)
    elif(cmd == "size"):
        print(q.qsize())
    elif(cmd == "empty"):
        print(1 if q.empty() else 0)
    elif(cmd == "front"):
        print(q.queue[0] if not q.empty() else -1)
    elif(cmd == "back"):
        print(q.queue[-1] if not q.empty() else -1)