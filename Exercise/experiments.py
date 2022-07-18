from tempfile import tempdir


def group(numbers):
    temp = []
    result = []

    temp.append(numbers[0])
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            temp.append(numbers[i])

            if i == len(numbers) - 1:
                result.append(temp.copy())
        else:
            result.append(temp.copy())
            temp.clear()
            temp.append(i)

            if i == len(numbers) - 1:
                result.append(temp.copy())

    return result

def max_consecutive(items):
    max = 0
    sequence = group(items)

    for element in sequence:
        if len(element) > max:
            max = len(element)

    return max

print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))