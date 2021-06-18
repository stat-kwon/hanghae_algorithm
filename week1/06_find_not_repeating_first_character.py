input = "adbacabade"


def find_not_repeating_character(string):
    check_list = [0] * 26

    for char in input:
        if not char.isalpha():
            continue
        else:
            alphabet_index = ord(char) - ord('a')
            check_list[alphabet_index] += 1
    print(check_list)
    not_repeating_character_array = []
    for index in range(len(check_list)):
        alphabet_occurence = check_list[index]
        if alphabet_occurence == 1:
            not_repeating_character_array.append(chr(index+ord("a")))
    print(not_repeating_character_array)
    for char in string:
        if char in not_repeating_character_array:
            return char


result = find_not_repeating_character(input)
print(result)
