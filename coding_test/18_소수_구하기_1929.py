import sys

sys.stdin = open('./txt/problem_18.txt', 'rt')

M, N = map(int, input().split())


def check_number(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


for i in range(M, N + 1):
    if check_number(i):
        print(i)

''' 문제 이해하기
1. M 이상 N이하의 소수를 모두 출력
2. 한줄에 하나씩 증가하는 순서대로 소수를 출력
'''

## 시간초과
# def answer_number(num):
#     check_list = [0] * (num + 1)
#     data = []
#     for i in range(2, len(check_list) - 1):
#         if check_list[i] == 0:
#             data.append(i)
#             for j in range(i, num + 1, i):
#                 check_list[j] = 1
#     return data
#
#
# for i in answer_number(N):
#     if i not in answer_number(M):
#         print(i)

''' 최대한 append를 안쓰는 방향으로 코딩하는게 맞고 int(number**0.5)+1 <- 이건 소수 구할때 시간 줄이는 팁 이므로 알고 있어야 할듯'''
