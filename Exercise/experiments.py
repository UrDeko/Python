def sum_of_numbers(st):
    sum = 0
    number = ""
    for i in range(len(st)):
        if st[i].isnumeric():
            number += st[i]
            if i == len(st) - 1:
                sum += int(number)
        else:
            if number:
                sum += int(number)
                number = "" 

    return sum

st = "ab5"
print(dir(st))