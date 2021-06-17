import sys

sys.stdin = open('./txt/problem_22.txt', 'rt')

N = int(sys.stdin.readline())

stack = []
for i in range(N):
    order = list(map(str, input().split()))
    if order[0] == 'push':
        stack.append(int(order[1]))
    elif order[0] == 'pop':
        if stack:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    else:
        if not stack:
            print(-1)
        else:
            print(stack[-1])
