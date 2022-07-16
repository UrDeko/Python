from logging import raiseExceptions


class Bill:
    def __init__(self, amount):
        if amount < 0 or not isinstance(amount, int):
            raise TypeError("Input not valid")
        else:
            self.amount = amount

    def __str__(self):
        return f"{self.amount}$"

    def __repr__(self):
        return f"A {self.amount}$ bill"

    def __int__(self):
        return self.amount  

    def __eq__(self, object):
        if isinstance(object, Bill):
            return self.amount == object.amount

        return False

    def __hash__(self):
        return hash(self.amount)


class BillBatch:
    def __init__(self, list_of_bills):
        self.list_of_bills = list_of_bills

    def __len__(self):
        return len(self.list_of_bills)

    def __getitem__(self, index):
        return self.list_of_bills[index]

    def total(self):
        sum = 0

        if self.list_of_bills:
            for element in self.list_of_bills:
                sum += element.amount
        
        return sum


class CashDesk:

    def __init__(self):
        self.desk = {10: 0, 20: 0, 50: 0, 100: 0}

    def get_bills_quantity(self, batch):
        bills = {10: 0, 20: 0, 50: 0, 100: 0}

        for element in batch:
            bills[int(element)] += 1
        
        return bills

    def take_money(self, money):

        if isinstance(money, BillBatch):
            self.desk = self.get_bills_quantity(money)
        else:
            self.desk[int(money)] += 1

    def withdraw(self, amount):
        bills_values = list(self.desk.keys())
        bills_count = list(self.desk.values())
        take = [0] * 4

        for i in range(3, -1, -1):
            take[i] = min(bills_count[i], amount // bills_values[i])
            amount -= take[i] * bills_values[i]

        if amount == 0:
            take = dict(zip(self.get_bills_quantity([]).keys(), take))

            for element in self.desk:
                self.desk[element] -= take[element]

        return [-1] if amount else self.desk
               
    def total(self):
        sum = 0

        for element in self.desk:
            sum += self.desk[element] * element

        return sum

    def inspect(self):
        for bill in self.desk:
            print(f"{bill}$ - {self.desk[bill]}")

#values = [10, 20, 50, 100]
#bills = [Bill(value) for value in values]
#batch = BillBatch(bills)
#
#for bill in batch:
#    print(bill)

values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]
batch = BillBatch(bills)
desk = CashDesk()

desk.take_money(batch)
desk.take_money(Bill(10))
print(desk.total())
desk.inspect()

desk.withdraw(30)
print(desk.total())
desk.inspect()




