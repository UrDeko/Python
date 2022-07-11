number = -10

# sumDigits = 0

# sumDigits = number % 10
# number = number // 10
# sumDigits += number % 10
# number = number // 10
# sumDigits += number
# print(sumDigits)

def sumDigits(number):
    sum = 0
    num_positive = abs(number)
    digits_count = len(str(num_positive))

    for i in range (0, digits_count):
        sum += num_positive % 10
        num_positive //= 10

    return sum

print(sumDigits(number))