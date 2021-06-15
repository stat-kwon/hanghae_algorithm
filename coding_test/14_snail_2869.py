import sys
import math
sys.stdin = open('problem_14.txt', 'rt')
import math
A, B, V = map(int, input().split())

# 시간초과
#
# street=0
# cnt = 0
# while True:
#     cnt += 1
#     street += A
#     if street >= V:
#         print(cnt)
#         break
#     street -= B

# before_day = V-A
# if before_day % (A-B) == 0:
#     count = int(before_day/(A-B))
# else:
#     count = int(before_day/(A-B)+1)
# print(count+1)
before_day = V-A
count = math.ceil(before_day/(A-B))
print(count+1)