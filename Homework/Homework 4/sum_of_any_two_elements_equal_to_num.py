def func(some_list, num):
    sum = 0
    result = ()

    for i in range(len(some_list)):
        for j in range(i + 1, len(some_list)):
            sum = some_list[i] + some_list[j]
            if sum == num:
                result += ([some_list[i], some_list[j]],)
    
    return result

def func2(some_list, num):
    low = 0
    high = len(some_list) - 1
    pairs = ()

    while low < high:
        if some_list[low] + some_list[high] < num:
            low += 1
        elif some_list[low] + some_list[high] == num:
            pairs += ((some_list[low], some_list[high]), )
            high -= 1
        else:
            high -= 1
    
    return pairs


print(func2([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))