from os import name
from hero import Hero
from orc import Orc
import random

def create_player():
    print("Choose your hero:\nHero: Health - 200, damage - 30\nOrc: Health - 150, damage - 30, berserk factor - 1.5")
    hero = input()
    nickname = input("Select nickname: ")
    if hero == "Orc":
        player = Orc(nickname, 100, 20, 1.5)
    if hero == "Hero":
        player = Hero(nickname, 100, 30, "The conqueror")
    return player

def draw_turn():
    turn = random.randint(1, 2)
    order = 0
    if turn == 1:
        order = range(1, 3)
    if turn == 2:
        order = range(2, 0, -1)
    return order

def battle(player1, player2):
    order = draw_turn()

    while player1.get_health() > 0 and player2.get_health() > 0:
        for i in order:
            if i == 1:
                if not player1.is_alive():
                    break
                message = input(f"{player1.get_name()}: Attack! or Heal! ")
                if message == "Attack":
                    player1.attack(player2)
                    print(f"{player1.get_name()} hit {player2.get_name()}! {player2.get_name()} health - {player2.get_health()}")
                else:
                    player1.take_healing(int(input("Potion: ")))
                    print(f"Aaaah that's better! {player1.get_name()} health status - {player1.get_health()}")
            elif i == 2:
                if not player2.is_alive():
                    break
                message = input(f"{player2.get_name()}: Attack! or Heal! ")
                if message == "Attack":
                    player2.attack(player1)
                    print(f"{player2.get_name()} hit {player1.get_name()}! {player1.get_name()} health - {player1.get_health()}")
                else:
                    player2.take_healing(int(input("Potion: ")))
                    print(f"Aaaah that's better! {player2.get_name()} health status - {player2.get_health()}")
    
    if player1.is_alive():
        print(f"{player1.get_name()} WINS!")
    else:
        print(f"{player2.get_name()} WINS!")

player1 = create_player()
player2 = create_player()

battle(player1, player2)