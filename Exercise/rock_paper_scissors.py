import random

#options = ["Rock", "Paper", "Scissors"]
#index = random.randint(0, 2)

computer = random.choice(["Rock", "Paper", "Scissors"])
user = input("Rock, Paper or Scissors?\n")

if user == computer:
    print("TIE")
elif user == "Rock" and computer == "Scissors":
    print("WIN")
elif user == "Paper" and computer == "Rock":
    print("WIN")
elif user == "Scissors" and computer == "Paper":
    print("WIN")
else:
    print("LOSE")