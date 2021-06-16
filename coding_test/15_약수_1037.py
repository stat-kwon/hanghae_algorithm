import sys

sys.stdin = open('./txt/problem_15.txt', 'rt')

N = int(input())  # 약수의 개수
common = list(map(int, input().split()))
print(max(common)*min(common))