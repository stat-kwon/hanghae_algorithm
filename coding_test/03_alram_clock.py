import sys

sys.stdin = open("problem_03.txt", 'rt')

hour, minit = map(int, input().split())


def clock(hour, minit):
    if minit - 45 < 0:
        if hour == 0:
            hour = 23
            minit = 60 + minit - 45
        else:
            minit = 60 + minit - 45
            hour = hour - 1
    else:
        minit = minit - 45
    return print(hour, minit)


clock(hour, minit)
