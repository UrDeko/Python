def get_numbers_count(numbers):
    numbers_count = {}
    numbers_count2 = {number: numbers.count(number) for number in numbers}

    #for number in numbers:
    #    if numbers_count.get(number):
    #        numbers_count[number] += 1
    #    else:
    #        numbers_count[number] = 1

    for number in numbers:
        try:
            numbers_count[number] += 1
        except KeyError:
            numbers_count[number] = 1

    return numbers_count

print(get_numbers_count([1, 2, 2, 4, 6, 7, 7]))