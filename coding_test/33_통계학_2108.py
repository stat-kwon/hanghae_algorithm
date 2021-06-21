import sys

sys.stdin = open('./txt/problem_33.txt', 'rt')

N = int(input())
values = []
for _ in range(N):
    values.append(int(input()))


class cul():

    def __init__(self, values):
        self.values = values

    def mean(self):
        return round(sum(self.values) / len(values))

    def mid(self):
        sorted_values = sorted(self.values)
        return sorted_values[len(self.values) // 2]

    def max_count(self):
        dis_num = set(self.values)
        check_list = {key: 0 for key in dis_num}

        for i in self.values:
            check_list[i] += 1

        sort_dic = sorted(check_list.items(), key=lambda x: x[0], reverse=True)

        if N != 1:
            if sort_dic[0][-2] == sort_dic[1][-2]:
                return sort_dic[1][-1]
            else:
                return sort_dic[0][-1]
        else:
            return sort_dic[0][-1]

    def num_range(self):
        sorted_values = sorted(self.values)
        return sorted_values[-1] - sorted_values[0]


a = cul(values)
print(a.mean())
print(a.mid())
print(a.max_count())
print(a.num_range())

'''
class cul():

    def __init__(self, values):
        self.values = values

    def mean(self):
        return round(sum(self.values) / len(values))

    def mid(self):
        sorted_values = sorted(self.values)
        return sorted_values[len(self.values) // 2]

    def max_count(self):
        dis_num = set(self.values)
        check_list = {key:0 for key in dis_num}
        for i in self.values:
            check_list[i] += 1

        max_num = -2147
        max_list = []
        for i in check_list.items():
            if i[1] > max_num:
                max_num = i[1]

        for i in check_list.items():
            if i[1] == max_num:
                max_list.append(i[0])
        if len(sorted(max_list)) == 1:
            return sorted(max_list)[0]
        else:
            return sorted(max_list)[1]


    def num_range(self):
        sorted_values = sorted(self.values)
        return sorted_values[-1] - sorted_values[0]
'''

# input = [2, 2, 2, 5, 5, 5, 6, 6, 6, 6, 6, 6, 9, 9, 11, 11, 11, 11, 11, 11]
#
# max_input = max(input)
# my_list = [0] * (max_input+1)
# print(my_list)  # 11개가 생김
# for i in input:
#     my_list[i] += 1  # input의 값을 my_list의 index라고 하고 나올때마다 +1하는 것이다.
#     # i-1을 하는 이유는 파이썬의 index는 0부터 시작하기 때문이다.
#     # 즉 input의 1의 값은 my_list의 첫번째 index인 0번 index에서 +1을 하기위해서이다.
# print(my_list)
# # [0, 3, 0, 0, 3, 6, 0, 0, 2, 0, 6]
# # 2-3번, 5-3번, 6-6번, 9-2번, 11-6번 나옴
#
# # -------------경우1, 2의 다른 부분----------------#
# num = 0  # 최빈값의 개수
# my_most = 0  # 최빈값을 알기 위한 변수 -my_list의 위치 반환
# for k in my_list:
#     my_most += 1  # my_list의 위치값 = input의 값
#     if k == max(my_list):
#         num += 1  # 최빈값이 나올때만 증가시킴
#         print('input 리스트에서, 여러 최빈값중 %d번째 최빈값은 %d 이며, 총 %d번 나왔다.'
#               % (num, my_most, max(my_list)))
#
# print('이 input리스트에서 최빈값의 개수는 %d개 이다' % num)
# ------------------------------------------------#

