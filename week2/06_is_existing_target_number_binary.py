finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    left_index = 0
    right_index = len(array) - 1
    current_mid = (left_index + right_index) // 2
    finding_count = 0

    while right_index >= left_index:
        finding_count += 1
        if array[current_mid] == target:
            print(finding_count)
            return True
        elif array[current_mid] < target:
            left_index = current_mid + 1
        else:
            right_index = current_mid - 1
        current_mid = (left_index + right_index) // 2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
