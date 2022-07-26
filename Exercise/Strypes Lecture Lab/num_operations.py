def operations(num):

    operation_number = input("Operation and number: ")
    while True:
        try:
            num = eval(f"{num} {operation_number}")
        except (NameError, ZeroDivisionError):
            return num

        operation_number = input("Operation and number: ")
        
        
def operations2(file):
    num1 = 0
    with open(file, "r") as file:
        input = list(file.readlines())
        num1 = int(input[0])
        for i in range(1, len(input)):
            try:
                num1 = eval(f"{num1} {input[i]}")
            except (NameError, ZeroDivisionError):
                return num1

        return num1

print(operations2("C:\\Users\\Deko\\Documents\\Work\\Python\\Exercise\\Strypes Lecture Lab\\operations.txt"))
print(operations(5))

#num1 = 0
#with open(file, "r") as file:
#   num1 = int(file.readline())
#   line = file.readline()
#   while line != "":
#       try:
#           num1 = eval(f"{num1} {line}")
#       except (NameError, ZeroDivisionError):
#           return num1
#       line = file.readline()
#    return num1