import time

start_time = time.time()

input2 = '123454321'  # string

cnt = 0


def is_palindrome(string):
    global cnt
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    print('스택 IN -> string:{} cnt:{}'.format(string, cnt))
    is_palindrome(string[1:-1])
    cnt += 1
    print('스택 OUT -> string:{} cnt:{}'.format(string, cnt))


print(is_palindrome(input2))

end_time = time.time()
print()
print("시간 측정: {:.10f}".format(end_time - start_time))
