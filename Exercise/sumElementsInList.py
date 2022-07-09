list = [1, 2, 3, 4, 5]

def sumElements(list):
    result = 0

    for i in range (0, len(list)):
        result += list[i]
    
    return result

print(sumElements(list))