import random
import time
import ascii_art as art


suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {
    'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
    'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11
}

playing = True
opponents = ['Xiphosian','Berdan','Devonie','Dealer']
players = ['Xiphosian','Berdan','Devonie','Dealer']
all_hands = {
    'Dealer' : {'hand' : [], 'point' : 0, 'bank' : 300, 'bet':0},
    'Xiphosian' : {'hand' : [], 'point' : 0, 'bank' : 300, 'bet':0},
    'Berdan' : {'hand' : [], 'point' : 0, 'bank' : 300, 'bet':0},
    'Devonie' : {'hand' : [], 'point' : 0, 'bank' : 300, 'bet':0}
}
temporary_hand = []
deck = []
temporary_deck=()

controller=[]
print(art.casino)
print('\n')
time.sleep(0.7)
print("Welcome to the Jackson's Casino\n")
print('BlackJACK game will begin in a minute\n')
print(f'{art.deck[8]} {art.deck[12]}\n')
time.sleep(1)

def deck_creater():
    for suit in suits:
        for rank in ranks:
            temporary_deck=(suit,rank)
            deck.append(temporary_deck)




def deck_shuffle():
    random.shuffle(deck)

def hit(source,target):

    temporary_hand=all_hands[target]['hand']
    temporary_hand.append(source.pop())
    all_hands[target]['hand'] = temporary_hand    
    temporary_hand=[]
    

def bet_to_game(player,bet):

    all_hands[player]['bank']-=bet
    all_hands[player]['bet']+=bet

def show_hand(username):
    dealer_card=all_hands['Dealer']['hand'][0]
    print(f"The Dealer's first card is: {dealer_card[0]} of {dealer_card[1]}")
    print(art.deck[ranks.index(dealer_card[1])])
    print('\n')
    user_hand=all_hands[username]['hand']
    print('Your hand:\n')

    for card in user_hand:
        print(art.deck[ranks.index(card[1])])
        print(f'{card[0]} of {card[1]}')

def show_winning_hand(winner):

    print(f'{winner} win the game!\n')
    user_hand=all_hands[winner]['hand']
    for card in user_hand:
        print(art.deck[ranks.index(card[1])])
        print(f'{card[0]} of {card[1]}')

def give_price(winner):
    total_bet=0
    for player in players:
        total_bet += all_hands[player]['bet']
        all_hands[player]['bet']=0

    all_hands[winner]['bank'] += total_bet
        


def show_balance():
    for player in players:
        bank = all_hands[player]['bank']
        print(f'{player} has {bank} dolar in bank!\n')


def join_game(username,bank):
    join_hand={'hand':[]}
    join_hand['point']=0
    join_hand['bank']=bank
    join_hand['bet']=0
    all_hands[username]=join_hand
    players.append(username)

def calculate_point():
    for player in players:
        hand_sum = 0
        temporary_hand=all_hands[player]['hand']
        for i in range(0,len(temporary_hand)):

            hand_sum += values[temporary_hand[i][1]]
        all_hands[player]['point']=hand_sum


def calculate_player(player):
    hand_sum = 0
    temporary_hand=all_hands[player]['hand']
    for i in range(0,len(temporary_hand)):
        hand_sum += values[temporary_hand[i][1]]
    all_hands[player]['point']=hand_sum

username = input('Please give your name for joining game!\n')
user_bank = int(input('Please give your current bank cash\n'))
join_game(username,user_bank)

while playing == True:

    bet_is_bet=True
    user_turn = True
    deck_creater()
    time.sleep(0.4)
    deck_shuffle()

    for player in players:
        for i in range(0,2):
            hit(deck,player)

    calculate_point()
    
    show_balance()
    while bet_is_bet==True:
        user_bet = int(input('How much are you going to bed?\n'))
        if user_bet > all_hands[username]['bank']:
            bank = all_hands[username]['bank']
            print(f'Please take a bet below your current cash in the bank: {bank}\n')
        else:
            bet_is_bet=False

    for player in players:
        bank=all_hands[player]['bank']
        if user_bet >= all_hands[player]['bank']:
            all_in = all_hands[player]['bank']
            print(f'{player} is going to bet all in!\n')
            bet_to_game(player,all_in)
        else:
            bet_to_game(player,user_bet)
    
    show_hand(username)
    
    for opponent in opponents:
        while all_hands[opponent]['point']<17:
            hit(deck,opponent)
            calculate_player(opponent)
            if all_hands[opponent]['point'] >= 17 :
                if all_hands[opponent]['point'] <= 21:
                    print(f'{opponent} Stand!\n')
                    break
                else:
                    break
    
    while user_turn == True:
        if all_hands[username]['point'] <= 21:
            user_choice = input('Do you want to hit or stand?\n Press "h" for hit "s" for stand!\n').lower()

            if user_choice == 'h':
                hit(deck,username)
                calculate_player(username)
                show_hand(username)
            else:
                user_turn = False
        else:
            print(f'{username} Busted!\n')
            user_turn = False
    
    calculate_point()

    for i in range(0,len(players)-1):

        if all_hands[players[i]]['point'] > 21:
            print(f'{players[i]} Busted!\n')
        else:
            if (all_hands[players[i+1]]['point'] <= 21 and all_hands[players[i+1]]['point'] > all_hands[players[i]]['point'] ):
                controller = i+1
            else:
                controller = i
    
    show_winning_hand(players[controller])
    give_price(players[controller])
    
    time.sleep(2)

    show_balance()
    
    is_play_again = input('Do you want to play again! Press "y" for YES "n" for NO!\n').lower()

    if is_play_again == 'y':
        print("Let's ROLL!\n")
    else:
        playing = False
        print('Good Day!\n')


    
    
