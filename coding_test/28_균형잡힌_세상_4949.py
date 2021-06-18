import sys
sys.stdin = open('./txt/problem_28.txt', 'rt')


check_type = ['(', ')', '[', ']', '.']
while True:
    stack = []
    string = input()
    print(string)

    if string == '.':
        break

    for i in string:
        if i in check_type:
            stack.append(i)
            if len(stack) == 1:
                continue
            if stack[-2] == '(' and stack[-1] == ')':
                stack.pop()
                stack.pop()
                continue
            if stack[-2] == '[' and stack[-1] == ']':
                stack.pop()
                stack.pop()
    if len(stack) > 1:
        print('no')
    else:
        print('yes')
