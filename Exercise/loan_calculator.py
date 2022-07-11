loan = float(input("Loan: "))
interest = float(input("Interest: "))
monthly_payment = float(input("Monthly payment: "))
Period = int(input("Period: "))

monthly_rate = interest / 100 / 12

for i in range(Period):

    loan += (loan * monthly_rate)

    if loan - monthly_payment <= 0:
        print("The last payment is", loan)
        print("You paid off the loan in", i + 1, "months")
        break

    loan -= monthly_payment

    print("Paid", monthly_payment, "of which", interest, "was interest", end = " ")
    print("Now I owe", loan)