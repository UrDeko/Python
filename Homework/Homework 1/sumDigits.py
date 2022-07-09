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
    numPositive = abs(number)
    digitsCount = len(str(numPositive))

    for i in range (0, digitsCount):
        sum += numPositive % 10
        numPositive //= 10

    return sum

print(sumDigits(number))