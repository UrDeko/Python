def contains_digit(number, digit):
    digits = []
    digits_count = len(str(number))

    for i in range(digits_count):
        digits.insert(0, number % 10)
        number //= 10
    
    if digits.count(digit) > 0:
        return True
    
    return False

print(contains_digit(12346789, 5))
