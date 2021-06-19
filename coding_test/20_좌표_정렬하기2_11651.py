# # https://www.acmicpc.net/problem/11651

import sys

# sys.stdin = open('./txt/problem_20.txt', 'rt')

N = int(sys.stdin.readline())
check_list = []
for i in range(N):
    x, y = map(int, input().split())
    check_list.append([x, y])

check_list.sort(key=lambda x: (x[1], x[0]))
for i in check_list:
    print(*i)

''' 문제 이해하기
2차원 평면 위의 점 N개가 주어짐
좌표를 y좌표가 증가하는 순으로
y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력
점의 수 : N
i번점의 위치 x_i와 y_i
'''
