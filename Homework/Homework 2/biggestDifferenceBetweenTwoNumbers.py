def biggestDifference(arr):
    biggestDifference = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            difference = arr[i] - arr[j]
            if abs(difference) > abs(biggestDifference):
                biggestDifference = difference

    return biggestDifference

arr = [-10, -9, -1]
print(biggestDifference(range(100)))