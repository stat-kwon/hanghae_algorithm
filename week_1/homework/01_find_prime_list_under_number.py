import os

input = 20


def find_prime_list_under_number(number):
    check_list = [0] * (number + 1)
    answer = []

    for i in range(1, number + 1):
        if number % i == 0:
            check_list[i] += 1
    for i in range(len(check_list)):
        if check_list[i] == 0:
            answer.append(i)
    return answer[1:]



result = find_prime_list_under_number(input)
print(result)
