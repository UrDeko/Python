import numbers


def biggest_difference(numbers):
    biggest_difference = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            difference = numbers[i] - numbers[j]
            if abs(difference) > abs(biggest_difference):
                biggest_difference = difference

    return biggest_difference

numbers = [-10, -9, -1]
print(biggest_difference(range(100)))