# https://www.acmicpc.net/problem/2839
# 생각보다 안풀렸던 문제^^ 문제 이해 필요

import sys
sys.stdin = open('problem_10.txt', 'rt')

kg = int(input())

cnt = 0
while kg >= 0:
    if kg % 5 == 0:
        cnt += kg // 5
        print(cnt)
        break
    kg -= 3
    cnt += 1
else:
    print(-1)
