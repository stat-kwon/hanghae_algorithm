input = "hello my name is sparta"


def find_max_occurred_alphabet(input):
    check_list = [0] * 26

    for char in input:
        if not char.isalpha():
            continue
        else:
            alphabet_index = ord(char) - ord('a')
            check_list[alphabet_index] += 1

    max_alphabet = 0
    max_alphabet_index = 0
    for index in range(len(check_list)):
        alphabet_occurence = check_list[index]

        if alphabet_occurence > max_alphabet:
            max_alphabet = alphabet_occurence
            max_alphabet_index = index

    return chr(max_alphabet_index + ord("a"))


result = find_max_occurred_alphabet(input)
print(result)