import sys

sys.stdin = open('problem_11.txt', 'rt')

# ''' 생각 정리하기 '''
# # 0지점에서 3지점까지 이동 0 1 2 3
# # 111
# # 0지점에서 4지점까지 이동 0 1 2 3 4
# # 1 2 1
# # 1지점에서 5지점까지 이동 1 2 3 4 5
# # 5-1 =4 121
# # 45지점에서 50지점까지 이동
# # 50-45 = 5
# # 1 1 2 1
#
# # 규칙을 찾아보자
# # 1     1
# # 11    2
# # 111   3
# # 121   4
# # 1211  5
# # 1221  6
# # 12211 7
# # 12221 8
# # 12321 9
# # 123211 10
#
# x = 45
# y = 100
# # 이동해야하는 거리
# total = y - x
# print(total)
# # 123456 => 21
# # 123456/54321 21+15
# # 12345 => 15
# # 어쨋든 //2한것을 넘으면 다시는 못돌아감
# # 12345/4321 25 + 10이 빔 따라서 4321 재료를 가지고 10을 만들어주어야 최소가 될듯
# # 1 2 3 4 5/4 4 4 3 2 2 1 11번만에 최소로 가게됨
#
# rule = total // 2
#
# cnt = 0
# increase = 0
#
# while True:
#     increase += 1
#     cnt += increase
#     if (cnt + increase + 1) > rule:
#         break
# print(increase, cnt)
#
# # cnt-increase
# namugi = total - cnt - (cnt - increase)
# namugi_cnt = namugi//(increase-1)+1
# # print(namugi)
# # print(namugi//(increase-1)+1)
#
# print(increase +(increase-1)+namugi_cnt)

'''두번째 시도'''
# N = int(input())
# for i in range(N):
#     x, y = map(int, input().split())
#
#     # 가야하는 거리 total
#     total = y - x
#     # 내가 정한 룰
#     rule = total // 2
#
#     # increase는 룰까지 사용되는 가장 큰 정수 / cnt는 합계
#     cnt = 0
#     increase = 0
#     while True:
#         increase += 1
#         cnt += increase
#         if (cnt + increase + 1) > rule:
#             break
#     print(increase, cnt)
#     namugi = total - cnt - (cnt - increase)
#     if increase-1 == 0:
#         namugi_cnt = namugi
#     else:
#         namugi_cnt = namugi//(increase-1)+1
#     print(increase + (increase - 1) + namugi_cnt)

'''3번째 시도도'''
N = int(input())
for i in range(N):
    x, y = map(int, input().split())

    # 가야하는 거리 total
    total = y - x
    # 내가 정한 룰
    rule = total // 2+1

    # increase는 룰까지 사용되는 가장 큰 정수 / cnt는 합계
    cnt = 0
    increase = 0
    while True:
        increase += 1
        cnt += increase
        if (cnt + increase + 1) > rule:
            break
    print(increase, cnt)
    namugi = total - cnt - (cnt - increase)
    if increase-1 == 0:
        namugi_cnt = namugi
    else:
        namugi_cnt = namugi//(increase-1)+1
    print(increase + (increase - 1) + namugi_cnt)
