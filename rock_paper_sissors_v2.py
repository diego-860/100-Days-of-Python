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

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

sissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

signals = [rock, paper, sissors]

players_move = int(input(
    'Choose your move: "0" = Rock, "1" = Paper, "2" = Sissors:\n'))

computers_move = random.randint(0, 2)

print(signals[players_move])
print(signals[computers_move])

if players_move >= 3 and players_move < 0:
    print("Invalid response - you lose!")
elif players_move == 0 and computers_move == 2:
    print("You win!")
elif players_move == 2 and computers_move == 0:
    print("You lose!")
elif players_move > computers_move:
    print("You win!")
elif players_move < computers_move:
    print("You lose!")
elif players_move == computers_move:
    print("It's a draw!")
