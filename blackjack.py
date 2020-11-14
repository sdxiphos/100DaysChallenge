import random
import time
import ascii_art as art


suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {
    'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
    'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11
}
ace_counter={
    'Dealer' : {'Ace' : {}},
    'Xiphosian' : {'Ace' : {}},
    'Berdan' : {'Ace' : {}},
    'Devonie' : {'Ace' : {}} 
}

opponents = ['Xiphosian','Berdan','Devonie','Dealer']
all_hands = {
    'Dealer' : {'hand' : [], 'point' : 0, 'bank' : 300, 'bet':0},
    'Xiphosian' : {'hand' : [], 'point' : 0, 'bank' : 300, 'bet':0},
    'Berdan' : {'hand' : [], 'point' : 0, 'bank' : 300, 'bet':0},
    'Devonie' : {'hand' : [], 'point' : 0, 'bank' : 300, 'bet':0}
}

playing = True
ace_control=False
winners=[]
temporary_hand = []
deck = []
temporary_deck=()
players=[]
controller=''
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


def control_winners(winner):
    winners=[]
    winners.append(winner)
    for player in players:
        if player != winner and all_hands[player]['point'] == all_hands[winner]['point']:
            winners.append(player)
        else:
            pass
    return winners


def show_winning_hand(winner):

    for winner in winners:
        print(f'{winner} win the game!\n')
        user_hand=[]
        user_hand=all_hands[winner]['hand']
        for card in user_hand:
            print(art.deck[ranks.index(card[1])])
            print(f'{card[0]} of {card[1]}')


def give_price(winners):

    total_bet = 0
    own_bet = 0
    for player in players:
        total_bet += all_hands[player]['bet']
        all_hands[player]['bet']=0
    for winner in winners:
        own_bet = int(total_bet/len(winners))
        all_hands[winner]['bank'] += own_bet
        


def show_balance():
    for player in players:
        bank = all_hands[player]['bank']
        print(f'{player} has {bank} dolar in bank!\n')


def user_join_game(username,bank):
    join_hand={'hand':[]}
    join_hand['point']=0
    join_hand['bank']=bank
    join_hand['bet']=0
    user_ace={'Ace':{}}
    all_hands[username]=join_hand
    ace_counter[username]=user_ace


def join_game(username):
    if all_hands[username]['bank'] > 0:
        players.append(username)
    
        for opponent in opponents:
            if all_hands[opponent]['bank'] > 0:
                players.append(opponent)
        if len(players) == 1:
            print("All opponent's account drain out!\n You win all the money!\ Good JOB!\n")
            return False
        else:
            remain_opponent=len(players)-1
            print(f'{remain_opponent} opponent remain!\n')
            return True

    else:
        print('You have no many in your bank.\n Leave this place!\n')
        return False



def calculate_point():
    for player in players:
        calculate_player(player)


def user_hit_stand(player):
    user_turn = True
    while user_turn == True:
        if all_hands[player]['point'] <= 21:
            user_choice = input('Do you want to hit or stand?\n Press "h" for hit "s" for stand!\n').lower()

            if user_choice == 'h':
                hit(deck,player)
                show_hand(player)
                calculate_player(player)

            else:
                user_turn = False
        else:
            busted_control(player)
            user_turn = False


def busted_control(player):
    print(f'{player} Busted!\n')
    players.remove(player)

    
def clear_data():
    players.clear()
    for player in all_hands:
        all_hands[player]['hand']=[]
        ace_counter[player]['Ace']={}
        all_hands[player]['point']=0


def calculate_player(player):
    hand_sum = 0
    temporary_hand=all_hands[player]['hand']
    ace_control=False
    previous_point = all_hands[player]['point']
    last_card = values[temporary_hand[-1][1]]
    new_point = last_card + previous_point

    def ace_justifier():
        global hand_sum
  

    for i in range(0,len(temporary_hand)):

        if temporary_hand[i][1]=='Ace':
            try:
                ace_value = ace_counter[player]['Ace'][i]
                if new_point > 21:
                    ace_counter[player]['Ace'][i]=1
                    hand_sum += 1
                else:
                    ace_counter[player]['Ace'][i]=11
                    hand_sum += 11      
                
            except:
                if new_point > 21:
                    ace_counter[player]['Ace'][i]=1
                    hand_sum += 1
                else:
                    ace_counter[player]['Ace'][i]=11
                    hand_sum += 11    
        else:
            hand_sum += values[temporary_hand[i][1]]

    all_hands[player]['point']=hand_sum



username = input('Please give your name for joining game!\n')
user_bank = int(input('Please give your current bank cash\n'))
user_join_game(username,user_bank)



while playing == True:
    bet_is_bet=True

    deck_creater()
    time.sleep(0.4)
    deck_shuffle()
    clear_data()

    if join_game(username) == False:
        print('GAME OVER!\n')
        playing=False
        break
    else:
        pass

    for player in players:
        for i in range(0,2):
            hit(deck,player)
    show_hand(username)
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
    
    for player in players:
        if player==username:
            user_hit_stand(player)
        else:
            while all_hands[player]['point']<17:
                hit(deck,player)
                calculate_player(player)
                if all_hands[player]['point'] >= 17 :
                    if all_hands[player]['point'] <= 21:
                        print(f'{player} Stand!\n')
                        break
                    else:
                        busted_control(player)
                        break
    
    calculate_point()

    winner = players[0]

    for i in range(0,len(players)-1):

        if all_hands[winner]['point'] > all_hands[players[i+1]]['point'] :
            winner = winner
        else:
            winner = players[i+1]
    
    winners =control_winners(winner)
    show_winning_hand(winners)
    give_price(winners)
    
    time.sleep(2)

    show_balance()
    
    is_play_again = input('Do you want to play again! Press "y" for YES "n" for NO!\n').lower()

    if is_play_again == 'y':
        print("Let's ROLL!\n")
    else:
        playing = False
        print('Good Day!\n')


    
    
