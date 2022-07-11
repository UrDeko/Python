def sum_of_numbers(st):
    result = ""
    sum = 0

    for i in range(len(st)):
        if st[i].isnumeric():
            result += st[i]
            if i == len(st) - 1 and result:
                sum += int(result)
        else:
            if result:
                sum += int(result)
                result = ""

    return sum

print(sum_of_numbers("ab"))