import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
stack = list()

for _ in range(n):
    cmd, *num = input().split()

    if(cmd == "push"):
        stack.append(int(num[0]))
    elif(cmd == "pop"):
        print(stack.pop() if len(stack) > 0 else -1)
    elif(cmd == "size"):
        print(len(stack))
    elif(cmd == "empty"):
        print(1 if len(stack) == 0 else 0)
    elif(cmd == "top"):
        print(stack[-1] if len(stack) > 0 else -1)