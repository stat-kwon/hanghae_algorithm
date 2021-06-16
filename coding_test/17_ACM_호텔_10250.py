import sys

sys.stdin = open('./txt/problem_17.txt', 'rt')

# 내가 만든 답???
for i in range(int(input())):
    H, W, N = map(int, input().split())

    floor_decision = N % H
    number_decision = N // H + 1
    if floor_decision == 0:
        floor_decision = H
        number_decision = N//H
    print(number_decision * 100 + floor_decision)


# 보고 찾은 답
# t = int(input())
#
# for i in range(t):
#     h, w, n = map(int, input().split())
#     num = n//h + 1
#     floor = n % h
#     if n % h == 0:  # h의 배수이면,
#         num = n//h
#         floor = h
#     print(f'{floor*100+num}')


''' 문제 이해
1. 가장 짧은 거리에 있는 방을 선호
2. 즉, 호텔 정문으로부터 거리가 가장 짧도록 방을 배정하는 프로그램
3. 호텔은 직사각형, 각 층에 W개의 방, H층의 건물 (1<=H,W<=99)
4. 엘리베이터는 가장 왼쪽. H*W 형태의 호텔, 호텔 정문은 1층 엘베 바로 앞
5. 거리가 같을 때는 아래층의 방을 더 선호
6. H W N <- H: 호텔의 층수 W: 각 층의 방의 수, N: 몇번 째 손님  H X W의 호텔
'''

''' 혼자 도달한 것
for i in range(int(input())):
    H, W, N = map(int, input().split())

    if N // H == 0:  # 사람이 층수보다 작은 경우
        number_decision = N
        floor_decision = 1
    elif N%H == 0:
        number_decision = H+1
        floor_decision = N//W
    else:
        number_decision = N // H + 1  # 번째 개념을 쓰기 때문에 +1 해줌
        floor_decision = N % H
    print(floor_decision*100+number_decision)
'''
