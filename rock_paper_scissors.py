#4. DAY
import random

game_on =True
rock_paper_scissors = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""","""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""","""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
while game_on == True:
    
    print('Welcome To The Ancient Game\n')
    print('ROCK PAPER SCISSORS\n')

    your_choice = int(input('Choose 0 for Rock, 1 for Paper, 2 for Scissors\n'))

    print('Your choice is: \n')
    print(rock_paper_scissors[your_choice])

    gamer_choice = random.randint(0,2)
    print(rock_paper_scissors[gamer_choice])

    if your_choice == 0:
        if gamer_choice == 1:
            print('You Lose!\n')
            restart_choice = input('Please write "y" for start the game, "n" for exit\n ').lower()
            if restart_choice != 'y':
                game_on=False
                print('See you again!\n')
            else:
                pass

        elif gamer_choice == 0:
            print('Draw!\n')
            restart_choice = input('Please write "y" for start the game, "n" for exit\n ').lower()
            if restart_choice != 'y':
                game_on=False
                print('See you again!\n')
            else:
                pass
        else:
            print('You win')
            restart_choice = input('Please write "y" for start the game, "n" for exit\n ').lower()
            if restart_choice != 'y':
                game_on=False
                print('See you again!\n')
            else:
                pass

    if your_choice == 1:
        if gamer_choice == 2:
            print('You Lose!\n')
            restart_choice = input('Please write "y" for start the game, "n" for exit\n ').lower()
            if restart_choice != 'y':
                game_on=False
                print('See you again!\n')
            else:
                pass

        elif gamer_choice == 1:
            print('Draw!\n')
            restart_choice = input('Please write "y" for start the game, "n" for exit\n ').lower()
            if restart_choice != 'y':
                game_on=False
                print('See you again!\n')
            else:
                pass            
        else:
            print('You win')
            restart_choice = input('Please write "y" for start the game, "n" for exit\n ').lower()
            if restart_choice != 'y':
                game_on=False
                print('See you again!\n')
            else:
                pass
            

    if your_choice == 2:
        if gamer_choice == 0:
            print('You Lose!\n')
            restart_choice = input('Please write "y" for start the game, "n" for exit\n ').lower()
            if restart_choice != 'y':
                game_on=False
                print('See you again!\n')
            else:
                pass
        elif gamer_choice == 2:
            print('Draw!\n')
            restart_choice = input('Please write "y" for start the game, "n" for exit\n ').lower()
            if restart_choice != 'y':
                game_on=False
                print('See you again!\n')
            else:
                pass
        else:
            print('You win')
            restart_choice = input('Please write "y" for start the game, "n" for exit\0n ').lower()
            if restart_choice != 'y':
                game_on=False
                print('See you again!\n')
            else:
                pass