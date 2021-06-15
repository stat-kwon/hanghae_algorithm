import sys

sys.stdin = open('problem_13.txt', 'rt')

n = int(input())

first = 666
while True:
    if '666' in str(first):
        n = n - 1
        if n == 0:
            break
    first = first + 1
print(first)
