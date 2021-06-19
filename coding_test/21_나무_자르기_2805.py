# # https://www.acmicpc.net/problem/2805

import sys

# sys.stdin = open('./txt/problem_21.txt', 'rt')

''' 문제 이해하기
1. 먼저, 상근이는 절단기에 높이 H를 지정해야 한다.
2. 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다.
3. 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구해라

입력
나무의 수 : N
집으로 가져가려고 하는 나무의 길이 : M
둘째줄은 나무의 높이
'''
import sys

N, M = map(int, sys.stdin.readline().split())

tree_list = list(map(int, sys.stdin.readline().split()))
max_num = max(tree_list)

left_inx = 1
right_inx = max_num
while left_inx <= right_inx:
    mid = (right_inx + left_inx) // 2

    cnt = 0
    for i in tree_list:
        if i >= mid:
            cnt += i - mid
        if cnt > M:
            break

    if cnt >= M:
        left_inx = mid + 1
    else:
        right_inx = mid - 1
print(right_inx)