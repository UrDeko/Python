seq1 = set()
seq1.add(45)
seq1.add(30)
seq1.add(60)

seq2 = {40, 50, 20}
seq3 = {50, 60, 30}

print(seq2 ^ seq3)

sequence = (1, 2, [22, 44], "a", 5, [55, 11], 1)

for element in sequence:
    if isinstance(element, list):
        for num in range(len(element)):
            element[num] = 0

print(sequence)

numbers = list(sequence)

for j in range(len(numbers)):
    if isinstance(numbers[j], str):
        numbers[j] = 1

modified_sequence = tuple(numbers)
print(modified_sequence)

sequence = modified_sequence

print(sequence)

queue = set(range(1, 49))

queue.update([4, 5, 66])
queue.update({0, 88, 93})

#print(help(queue.update))

queue_list = list(queue)
queue_squared = [x**2 for x in queue_list]

dict_comprehension = {val : val**2 for idx, val in enumerate(queue_list) if idx % 2 == 1 and val % 2 == 0}
print(dict_comprehension)