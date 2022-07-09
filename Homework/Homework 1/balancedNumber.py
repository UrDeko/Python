def is_number_balanced(number):
    digits = str(number)
    digitsCount = len(digits)
    sumLeft = 0
    sumRight = 0

    for i in range(digitsCount // 2):
        sumLeft += int(digits[i])
        sumRight += int(digits[digitsCount - 1 - i])
    
    if sumLeft == sumRight:
        return True
    else:
        return False

print(is_number_balanced(1238033))