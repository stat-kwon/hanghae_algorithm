import sys
sys.stdin = open('./txt/problem_09.txt', 'rt')

N = int(input())

def checker(string):
    cnt = 0
    duplicated_check = len(set(string))
    if len(string) <= 1:
        return True

    now = string[0]
    while string:
        string = string[1:]
        if len(string) == 1 and now == string[0]:
            cnt += 1
            break
        elif len(string) == 1 and now != string[0]:
            cnt += 2
            break
        if string[0] != now:
            now = string[0]
            cnt += 1

    if duplicated_check == cnt:
        return True
    else:
        return False

count = 0
for i in range(N):
    word = str(input())
    if checker(word):
        count += 1
print(count)
