def calculate_coins(sum):
    list = [100, 50, 20, 10, 5, 2, 1]
    number_of_coins = {1: 0, 2:0, 5:0, 10:0, 20:0, 50:0, 100:0}
    sum = int(sum * 100)

    for element in list:
        count = sum // element
        number_of_coins[element] = count
        sum -= element * count

    return number_of_coins

print(calculate_coins(8.94))