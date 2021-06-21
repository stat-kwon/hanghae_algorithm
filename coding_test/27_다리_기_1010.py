import sys

sys.stdin = open('./txt/problem_27.txt', 'rt')

''' 문제 이해하기
서쪽에는 N개의 사이트, 동쪽에는 M개의 사이트
'''

K = int(input())

def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

for _ in range(K):
    N, M = map(int, input().split())
    print(int(factorial(M)/factorial(N)/factorial(M-N)))
