#4. DAY
import random

game_on =True
test = [0,1,2]
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

def game_finish_control(game_winning_control):

    if game_winning_control=='d':
        print('Draw!\n')
    elif game_winning_control=='w':
        print('You Win!\n')
    else:
        print('You Lose!\n')


def game_start_control(game_winning_control):

    game_finish_control(game_winning_control)
    restart_choice = input('Please write "y" for start the game, "n" for exit\n ').lower()
    if restart_choice != 'y':
        return False
        print('See you again!\n')   
    else:
        return True


while game_on == True:
    
    print('Welcome To The Ancient Game\n')
    print('ROCK PAPER SCISSORS\n')

    your_choice = int(input('Choose 0 for Rock, 1 for Paper, 2 for Scissors\n'))

    print('Your choice is: \n')
    print(rock_paper_scissors[your_choice])

    gamer_choice = random.randint(0,2)
    print(rock_paper_scissors[gamer_choice])

    if test[your_choice-1] == gamer_choice :
        game_on = game_start_control('w')
    elif test[your_choice+1] == gamer_choice:
        game_on = game_start_control('l')
    else:
        game_on = game_start_control('d')



    # if your_choice == 0:
    #     if gamer_choice == 1:
    #         game_start_control('l')

    #     elif gamer_choice == 0:
    #         game_start_control('d')
    #     else:
    #         game_start_control('w')

    # if your_choice == 1:
    #     if gamer_choice == 2:
    #         game_start_control('l')

    #     elif gamer_choice == 1:
    #         game_start_control('d')         
    #     else:
    #         game_start_control('w')
            

    # if your_choice == 2:
    #     if gamer_choice == 0:
    #         game_start_control('l')

    #     elif gamer_choice == 2:
    #         game_start_control('d')

    #     else:
    #         game_start_control('w')