def to_digits(number):
    list = []
    digitsCount = len(str(number))
    
    for i in range(0, digitsCount):
        list.insert(0, number % 10)
        number //= 10

    return list

print(to_digits(123))