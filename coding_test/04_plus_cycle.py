import sys

sys.stdin = open("problem_04.txt", 'rt')

number = int(input())
first_number = number

cnt = 0
while True:
    sum_number = number // 10 + number % 10
    number = number % 10 * 10 + sum_number % 10
    cnt += 1
    if number == first_number:
        break
print(cnt)

# a = 124
# print(a%10)
