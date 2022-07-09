def containingAllDigits(number, digits):
    if not digits:
        return False

    numberAsList = []
    listLength = len(str(number))

    for i in range(listLength):
        numberAsList.insert(0, number % 10)
        number //= 10

    for element in digits:
        if numberAsList.count(element) > 0:
            continue
        else:
            return False
    
    return True

print(containingAllDigits(456, []))