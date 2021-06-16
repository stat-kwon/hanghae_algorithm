import sys

sys.stdin = open('./txt/problem_16.txt', 'rt')

num1, num2 = map(int, input().split())


def max_common(num1, num2):
    data = []
    if num1 > num2:
        for i in range(1, num1 + 1):
            if (num1 % i == 0) and (num2 % i == 0):
                data.append(i)
    else:
        for i in range(1, num2 + 1):
            if (num1 % i == 0) and (num2 % i == 0):
                data.append(i)
    return print(max(data), int(max(data) * (num1 / max(data)) * (num2 / max(data))), sep='\n')


max_common(num1, num2)

# 생각 정리
# 자기와 자신을 제외한 서로소를 일단 추출할듯
# 이후 공통 서로소를 최대공약수
# 나머지의 곱은 최소공배수
