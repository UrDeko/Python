def group(sequence):
    consecutive_elements = []
    result = []
    consecutive_elements.append(sequence[0])
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i + 1]:
            consecutive_elements.append(sequence[i + 1])
            if i + 1 == len(sequence) - 1:
                result.append(consecutive_elements.copy())
        else:
            result.append(consecutive_elements.copy())
            consecutive_elements.clear()
            consecutive_elements.append(sequence[i + 1])
            if i + 1 == len(sequence) - 1:
                result.append(consecutive_elements.copy())

    return result

def max_consecutive(items):
    max_sequence = 0
    sequences = group(items)

    for element in sequences:
        if len(element) > max_sequence:
            max_sequence = len(element)

    return max_sequence

print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 4]))
