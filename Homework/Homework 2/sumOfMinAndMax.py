def sumMinMax(list):
    min = 1000000
    max = -1000000

    for element in list:
        if element < min:
            min = element
        
        if element > max:
            max = element

    return min + max

list = [1]

print(sumMinMax(list))