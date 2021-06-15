# https://www.acmicpc.net/problem/4344
import sys

sys.stdin = open('problem_05.txt', 'rt')

C = int(input())


def average(array):
    return sum(array) / len(array)


for i in range(C):
    num = list(map(int, input().split()))
    score_array = num[1:]
    cnt = 0

    for j in score_array:
        if j > average(score_array):
            cnt += 1
    print('{:,.3f}%'.format((cnt / len(score_array) * 100)))
