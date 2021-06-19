import sys

sys.stdin = open('./txt/problem_24.txt', 'rt')

N = int(input())


def check_VPS():
    string = list(map(str, input()))
    stack = []
    for i in string:
        stack.append(i)
        if len(stack) == 1:
            continue
        if stack[-2] == '(' and stack[-1] == ')':
            stack.pop()
            stack.pop()
    if not stack:
        return print('YES')
    else:
        return print('NO')


for i in range(N):
    check_VPS()
