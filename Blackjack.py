import random


def deal(player_cards, dealer_cards):
    while len(player_cards) != 2 and len(dealer_cards) != 2:
        player_cards.append(random.randint(1,11))
        dealer_cards.append(random.randint(1,11))
    print("Dealer has", dealer_cards[1], "showing")
    print("You have", player_cards)

def play(player_cards):
    while True:
        pick = input("Do you want to hit or stay?")
        if pick == "hit":
            player_cards.append(random.randint(1,11))
            print("You now have" ,player_cards)

            if sum(player_cards) > 21:
                print("Bust, dealer wins")
                break
        
            elif sum(player_cards) == 21:
                print("Blackjack, you win")
                break
        else:
            break
            

def dealer(dealer_cards, player_cards):

    while sum(dealer_cards) < 17 and sum(player_cards) <= 21 :
        dealer_cards.append(random.randint(1,11))

    if sum(dealer_cards) == sum(player_cards):
        print("Dealer has", sum(dealer_cards), "and you have",sum(player_cards), " it is a Tie")

    elif sum(dealer_cards) > sum(player_cards) and sum(dealer_cards) <= 21:
        print("Dealer has" ,sum(dealer_cards), "dealer wins")

    elif sum(dealer_cards) > 21:
        print("Dealer busts, you win")


def main():
    player_cards = []
    dealer_cards = []

    deal(player_cards, dealer_cards)
    play(player_cards)
    dealer(dealer_cards,player_cards)

    

main()