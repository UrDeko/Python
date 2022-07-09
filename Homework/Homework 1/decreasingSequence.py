sequence = [1, 1, 1, 1]

def is_decreasing(seq):

    for i in range(1, len(seq)):
        if seq[i] < seq[i - 1]:
            continue
        else:
            return False

    return True

print(is_decreasing(sequence))