bills = []
billsNumber = int(input("Enter # of bills: "))

for i in range(billsNumber):
    bills.append(float(input("Enter bill: ")))

sum = 0
for bill in bills:
    sum += bill

print("Total: $", sum, sep = "")