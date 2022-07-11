def containing_all_digits(number, digits):
    if not digits:
        return False

    number_as_list = []
    listLength = len(str(number))

    for i in range(listLength):
        number_as_list.insert(0, number % 10)
        number //= 10

    for element in digits:
        if number_as_list.count(element) > 0:
            continue
        else:
            return False
    
    return True

print(containing_all_digits(456, []))