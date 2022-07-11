def to_digits(number):
    list = []
    digits_count = len(str(number))
    
    for i in range(0, digits_count):
        list.insert(0, number % 10)
        number //= 10

    return list

print(to_digits(123))