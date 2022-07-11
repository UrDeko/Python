def fib_number(n):
    num1 = 1
    num2 = 1
    result = ""

    if n > 0:
        if n == 1:
            result += str(num1)
        elif n == 2:
            result += str(num1) + str(num2)
        else:
            result += str(num1) + str(num2)
            for i in range(n - 2):
                nth = num1 + num2
                result += str(nth)
                num1 = num2
                num2 = nth

    return result

print(fib_number(7))