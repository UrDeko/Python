list = [1, 2, 3, 0, 2, 3]

def to_number(list):
    result = ""

    for i in range(0, len(list)):
        result += str(list[i])
    
    return int(result)

print(to_number(list))