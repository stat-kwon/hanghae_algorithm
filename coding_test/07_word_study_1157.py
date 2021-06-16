# https://www.acmicpc.net/problem/1157

import sys
sys.stdin = open('./txt/problem_07.txt', 'rt')

words = list(map(str,input().upper()))
word_dic ={key:0 for key in set(words)}

for word in words:
    word_dic[word] += 1
if len(words) != 1:
    if sorted(list(word_dic.values()))[-1] == sorted(list(word_dic.values()))[-2]:
        print('?')
    else:
        for key, value in word_dic.items():
            if value == sorted(list(word_dic.values()))[-1]:
                print(key)
else:
    print(words[0])


