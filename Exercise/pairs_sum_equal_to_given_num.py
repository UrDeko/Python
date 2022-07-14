def func(some_list, num):
    sum = 0
    result = ()

    for i in range(len(some_list)):
        for j in range(i + 1, len(some_list)):
            sum = some_list[i] + some_list[j]
            if sum == num:
                result += ([some_list[i], some_list[j]],)
                
    
    return result

tuple = (1, 2, 3)
print(func([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
#print(dir(tuple))