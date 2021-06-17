import sys
sys.stdin = open('./txt/problem_23.txt', 'rt')

K = int(input())

stack = []
for i in range(K):
    A = int(input())
    if A != 0:
        stack.append(A)
    else:
        stack.pop()
print(sum(stack))

''' 문제 이해하기
재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.
재민이는 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다.
'''