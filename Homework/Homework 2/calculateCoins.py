def calculateCoins(sum):
    list = [100, 50, 20, 10, 5, 2, 1]
    numberOfCoins = {1: 0, 2:0, 5:0, 10:0, 20:0, 50:0, 100:0}
    sum = int(sum * 100)

    for element in list:
        count = sum // element
        numberOfCoins[element] = count
        sum -= element * count

    return numberOfCoins

print(calculateCoins(8.94))