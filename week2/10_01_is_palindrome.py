input = "토마토"


def is_palindrome(string):
    n = len(string)
    rule = n//2
    for i in range(rule):
        if input[i] != input[-1-i]:
            return False
    return True


print(is_palindrome(input))