import sys

sys.stdin = open('./txt/problem_12.txt', 'rt')


def answer_count(num):
    cnt = 0
    check_list = [0] * (num + 1)

    for i in range(2, num + 1):
        if check_list[i] == 0:
            cnt += 1
            for j in range(i, num + 1, i):
                check_list[j] = 1
    return cnt

while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print(1)
else:
    print(answer_count(2 * n) - answer_count(n))


