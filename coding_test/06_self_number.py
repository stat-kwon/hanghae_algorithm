# https://www.acmicpc.net/problem/4673
n = 10000

def number_sum(num):
    gen = num
    while True:
        muk = num // 10
        namugi = num % 10
        gen += namugi
        num = muk
        if num == 0:
            break
    return gen

check_list = [0] * 2 * n
for i in range(1, n + 1):
    check_list[number_sum(i)] += 1

for i in range(len(check_list)):
    if check_list[i] == 0 and i != 0 and i < 10000:
        print(i)
