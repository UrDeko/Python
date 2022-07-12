def group(sequence):
    result = []
    consecutive_elements = []

    consecutive_elements.append(sequence[0])
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            consecutive_elements.append(sequence[i])
            if i == len(sequence) - 1:
                result.append(consecutive_elements.copy())
        else:
            result.append(consecutive_elements.copy())
            consecutive_elements.clear()
            consecutive_elements.append(sequence[i])
            if i == len(sequence) - 1:
                result.append(consecutive_elements.copy())

    return result

def max_consecutive(items):
    max_sequence = 0
    sequences = group(items)

    for element in sequences:
        if len(element) > max_sequence:
            max_sequence = len(element)

    return max_sequence

print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
