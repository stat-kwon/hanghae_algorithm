import sys

sys.stdin = open('./txt/problem_34.txt', 'rt')

N = int(input())

color = []
for _ in range(N):
    color.append(list(map(int, input().split())))
print(color)

mid = len(color) // 2
w_count = 0
b_count = 0

while mid <= 1:
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0
    for i in color[0:mid]:
        cnt1 += sum(i[0:mid])
    for i in color[0:mid]:
        cnt2 += sum(i[mid:])
    for i in color[mid:]:
        cnt3 += sum(i[0:mid])
    for i in color[mid:]:
        cnt4 += sum(i[mid:])

    if cnt1 == mid**2:
        b_count += 1
    elif cnt1 == 0:
        w_count += 1
    else:
        mid = mid//2



def half(_array):
    cnt1 = 0
    for i in color[0:4]:
        cnt1 += sum(i[0:4])
    if cnt1 != 16:


''' 문제 이해하기

'''
