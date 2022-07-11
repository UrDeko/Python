def is_number_balanced(number):
    digits = str(number)
    digits_count = len(digits)
    sum_left = 0
    sum_right = 0

    for i in range(digits_count // 2):
        sum_left += int(digits[i])
        sum_right += int(digits[digits_count - 1 - i])
    
    if sum_left == sum_right:
        return True
    else:
        return False

print(is_number_balanced(1238033))