import sys

sys.stdin = open('problem_08.txt', 'rt')

words = str(input())
croatia = ['c=', 'c-', 'dz=', 'd-', "lj", "nj", "s=", "z="]

cnt = 0
while words:
    if words[:3] == "dz=":
        words = words[3:]
        cnt += 1
    elif words[:2] in croatia:
        words = words[2:]
        cnt += 1
    else:
        words = words[1:]
        cnt += 1
print(cnt)
