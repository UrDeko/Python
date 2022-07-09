def primeInteger(number):
    if number == 1:
        return False

    sum = 0

    for i in range(1, number + 1):
        if number % i == 0:
            sum += i

    if sum == number + 1:
        return True

    return False

print(primeInteger(-10))