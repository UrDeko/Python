class DivideByZeroException(Exception):
    def __init__(self, message = "Division by zero"):
        super().__init__(message)

def div(num1, num2):
    result = 0
    try:
        if num2 == 0:
            raise DivideByZeroException()
        result = num1 / num2
    except DivideByZeroException:
        raise DivideByZeroException("You divided by zero!")
    except TypeError:
        raise TypeError("Division between number and string")

    return result

print(div(5, 0))