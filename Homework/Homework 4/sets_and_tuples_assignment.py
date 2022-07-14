sequence = set(range(0, 50))
sequence.update([4, 5, 66], {33, 0, 88})

numbers_list = list(sequence)
square_numbers_list = [x**2 for x in numbers_list]
square_numbers_dict = {val : val**2 for idx, val in enumerate(numbers_list)}
square_numbers_dict_constraint = {val : val**2 for idx, val in enumerate(numbers_list) if idx % 2 == 1 and val % 2 == 0}