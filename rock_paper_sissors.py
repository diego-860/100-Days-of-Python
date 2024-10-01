'''This is a Rock, Paper, Sissors module'''
import random
print('''
█▀█ █▀█ █▀▀ █▄▀  
█▀▄ █▄█ █▄▄ █░█  

█▀█ ▄▀█ █▀█ █▀▀ █▀█  
█▀▀ █▀█ █▀▀ ██▄ █▀▄  

█▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█

Welcome to Rock Paper Sissors!
''')
players_move = input(
    'Type "rock", "paper", or "sissors" to identify which signal you\'d like to deliver:')

signals = ["rock", "paper", "sissors"]

computers_move = random.choice(signals)

if players_move.lower() == "rock" and computers_move == "sissors":
    print("You won!")
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
elif players_move.lower() == "rock" and computers_move == "rock":
    print("It's a draw!")
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif players_move.lower() == "rock" and computers_move == "paper":
    print("You lost!")
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif players_move.lower() == "sissors" and computers_move == "paper":
    print("You won!")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif players_move.lower() == "sissors" and computers_move == "sissors":
    print("It's a draw!")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
elif players_move.lower() == "sissors" and computers_move == "rock":
    print("You lost!")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

elif players_move.lower() == "paper" and computers_move == "rock":
    print("You won!")
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif players_move.lower() == "paper" and computers_move == "paper":
    print("It's a draw!")
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif players_move.lower() == "paper" and computers_move == "sissors":
    print("You lost!")
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
