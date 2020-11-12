import ascii_art
import random
import time

bid=False
i=0
controller=0
auctioneer_bid=0
user_bid=0
winner=''
caller='Bid Caller'

lap=['First','Second','Third','Fourth']
auctioneers=['Xiphosian','Berdan','Devonie']
auction_bids={
    'Mona Lisa' : {'Bid Caller':250},
    'The Painter' : {'Bid Caller':110},
    'Venus de Milo' : {'Bid Caller':200},
    'The Queen of Nile' : {'Bid Caller':230}
}


def bid_update(item,auctioneer,bid):
    bidder={}
    bidder[auctioneer]=bid
    auction_bids[item].update(bidder)





print('WELCOME To The Auction House!\n')
print(ascii_art.auction_house)
print('\n')




username= input('Can you give your name to join the auction? \n')


for item in auction_bids:

    print(ascii_art.art_store[i])
    print('\n')
    time.sleep(0.6)
    print(f'{lap[i]} item in the auction is {item}\n')
    time.sleep(0.6)
    print(f'The Bid Caller start bids from {auction_bids[item][caller]} thousand dolars!\n')
    time.sleep(1)

    i += 1
    
    bid=False
    while bid == False:
        user_bid = int(input(f'Please give your first bid for {item}\n'))
        if user_bid <= auction_bids[item][caller]:
            print('Please bid higher than Bid Caller\n')
        else:
            bid_update(item,username,user_bid)
            bid=True
    for auctioneer in auctioneers:
        auctioneer_bid = random.randint(auction_bids[item]['Bid Caller']+1,400)
        bid_update(item,auctioneer,auctioneer_bid)
    for j in range(0,len(auctioneers)-1):
        if auction_bids[item][auctioneers[controller]] > auction_bids[item][auctioneers[j+1]]:
            controller = controller
        else:
            controller = j+1
    if user_bid > auction_bids[item][auctioneers[controller]]:
        
        print(f'{username} win the auction with {user_bid} thousand dolars for {item}!\n')
    else:
        print(f'{auctioneers[controller]} win the auction with {auction_bids[item][auctioneers[controller]]} thousand dolars for {item}!\n')
    
    time.sleep(2)


print('The auction is over!\n')
time.sleep(1)
print('Have a wonderful day!\n')

