list = [1, 2, 3, 4, 5]

def sum_elements(list):
    result = 0

    for i in range (0, len(list)):
        result += list[i]
    
    return result

print(sum_elements(list))