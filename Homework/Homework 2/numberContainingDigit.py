def containsDigit(number, digit):
    digits = []
    digitsCount = len(str(number))

    for i in range(digitsCount):
        digits.insert(0, number % 10)
        number //= 10
    
    if digits.count(digit) > 0:
        return True
    
    return False

print(containsDigit(12346789, 5))
