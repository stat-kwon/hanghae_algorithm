# filter 사용 예제 (약식 if문이라 생각하면 될듯)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x <= 5, a)))

# list comprehension 연습
a = [1, 2, 3]
b = [4, 5, 6]
dic = {key: value for key, value in zip(a, b)}
print(dic)

a = [str(n) + str(m) for n in ['수학', '영어', '과학'] for m in range(1, 11)]
print(a)
a = [f'{alpha}나는' + str(n) for alpha in ['A', 'B', 'C'] for n in range(1, 21)]
print(a)

# reduce 활용 예제
from functools import reduce

a = [1, 2, 3, 4, 5]
print(reduce(lambda init, x: init + x, a, 0))

a = [{'age': 10}, {'age': 15}, {'age': 5}]
print(reduce(lambda init, k: init + k['age'], a, 0))
