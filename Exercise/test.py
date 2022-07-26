import os

foods = ['spam', 'eggs', 'ham']
things = foods
things[1] = 'chips'

# [start: end: step]

cute_animals = ['cat', 'raccoon', 'panda', 'red panda', 'marmot']
cute_animals[1:3]
cute_animals[-1]
cute_animals[1:-1]
cute_animals[::-1]
cute_animals[-1 : 0 : -1]
cute_animals[-1 : 0 : -2]

#cute_animals.sort()
print(cute_animals[-1::-1])

#isdisjoint()

#s = "happy"
#b = s
#b = b.upper()
#print(s)
#
#def get_bills_quantity(batch):
#        bills = {10: 0, 20: 0, 50: 0, 100: 0}
#
#        for element in batch:
#            bills[int(element)] += 1
#        
#        return bills
#
#take = [1, 5, 10, 15]
#
#take = dict(zip(get_bills_quantity([]).keys(), take))
#
#for element in get_bills_quantity([]).keys():
#    print(element)

#list = [4, 3, 6, 7]
#iterator = iter(list)
#
#for i in sorted(iterator):
#    print(i)

#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))