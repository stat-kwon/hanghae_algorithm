import sys

sys.stdin = open('./txt/problem_25.txt', 'rt')

''' 문제 이해하기
두 자연수 A, B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성
T : test case
'''

T = int(input())


def max_common(num1, num2):
    LCM = num1 * num2
    for i in range(1, min(num1, num2) + 1):
        if (num1 % i) == 0 and (num2 % i) == 0:
            LCM = LCM // i
    return LCM


for i in range(T):
    A, B = map(int, input().split())
    print(max_common(A, B))

# def max_common(num1, num2):
#     data = []
#     for i in range(1,num2+1):
#         if (num1%i) == 0 and (num2%i) == 0:
#             data.append(i)
#     divide_common = 1
#     for i in data:
#         divide_common *= i
#     return int((num1/divide_common) * (num2/divide_common) * divide_common)
