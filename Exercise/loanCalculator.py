loan = float(input("Loan: "))
interest = float(input("Interest: "))
monthlyPayment = float(input("Monthly payment: "))
Period = int(input("Period: "))

monthlyRate = interest / 100 / 12

for i in range(Period):

    loan += (loan * monthlyRate)

    if loan - monthlyPayment <= 0:
        print("The last payment is", loan)
        print("You paid off the loan in", i + 1, "months")
        break

    loan -= monthlyPayment

    print("Paid", monthlyPayment, "of which", interest, "was interest", end = " ")
    print("Now I owe", loan)