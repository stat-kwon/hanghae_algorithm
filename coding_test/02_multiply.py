# https://www.acmicpc.net/problem/2588

import sys

sys.stdin = open('./txt/problem_02.txt', 'rt')

first = int(input())
second = list(map(int, input()))

mul_list = []
for i in second[::-1]:
    print(first * i)
    mul_list.append(first * i)

cnt = 0
total = 0
for i in mul_list:
    total += i * (10 ** cnt)
    cnt += 1
print(total)