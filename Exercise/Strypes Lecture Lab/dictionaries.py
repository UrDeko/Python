people = {"Sasho": 12, "Gosho": 13}
empty_dict = {}

#print(people)
people["Kiril"] = 42
#print(people)

for person in people:
    print(person, "is", people[person])

#for key, value in people.items():
#    print(key)
#    print(value)

#print(people.items())
#print(people.keys())
#print(people.values())

def sum_ages(people_ages, odd_numbers):
    sum = 0
    for person in people_ages:
        if not odd_numbers and people_ages[person] % 2 == 1:
            continue
        else:
            sum += people_ages[person]
    
    return sum

print(sum_ages(people, False))