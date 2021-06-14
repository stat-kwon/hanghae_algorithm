# https://www.acmicpc.net/problem/10869

import sys

sys.stdin = open('problem_01.txt', 'rt')
A, B = map(int, input().split())


class cul:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def add(self):
        return self.A + self.B

    def minus(self):
        return self.A - self.B

    def mul(self):
        return self.A * self.B

    def divide(self):
        if self.B == 0:
            return 0
        else:
            return self.A // self.B

    def namugi(self):
        return self.A % self.B


a = cul(A, B)
print(a.add())
print(a.minus())
print(a.mul())
print(a.divide())
print(a.namugi())
