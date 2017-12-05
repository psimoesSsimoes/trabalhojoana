#!python3.6
#coding: utf8

from card import Card
from deck import Deck
from player import Player
from dealer import Dealer

class Game:
    
    def __init__(self,player):
        self.you=player
        self.dealer=Dealer()

    def play(self):
        play='y'
        while you.can_play() and play=='y':
            lost=False
            try:
                bet=float(raw_input("how much you want to bet?"))
        
                if bet > you.balance():
                    bet=10.0 
            except ValueError:
            bet=10.0
            #player and dealer are just an array of Cards
            print("Bet of "+str(bet))
            deck=Deck(ReadDeck(str(which_deck)))
            #gives two cards
            for i in range(0,2):
                you.append(deck.popfromdeck())
                dealer.append(deck.popfromdeck())
             
            dealer.showgame()
            print("----------------------------------")
            you.showgame()

            if you.handpoints()!=21:
                while true:
                    answer = input("HIT OR STAND?")
                    if answer.lower()=="hit":
                        you.append(deck.popfromdeck())
                        you.showgame()
                        if you.handpoints() > 21:
                            print("PUMMMM! you have busted! Better Luck next Time!")
                            print("Lost "+str(bet))
                            you.update_balance(-bet)
                            lost=True
                            break
                        
                        elif you.handpoints()==21:
                            print("21! Yoaaah, you're in great shape!")
                            break
                        
                        else:
                            print("Your Points "+str(you.handpoints()))

                    else:
                        print("decided to stand. Dealer's Turn!")
                        break

            else:
                print("What a lucky hand! Blackjack you bastard!")
                print("Dealer's Turn!")
            
            if !lost:
                if dealer.handpoints()!=21:
                    while dealer.can_play():
                        dealer.append(deck.popfromdeck())
                        dealer.showgame()
                        print("Dealer's points: "+str(dealer.handpoints()))
                    
                    if dealer.handpoints() > 21:
                        print("House bursted!")
                        if you.handpoints()==21:
                            print("You win "+str(bet*3.0/2.0))
                            you.update_balance(bet*3.0/2.0)
                        else:
                            print("You win "+str(bet))
                            you.update_balance(bet)
                    else:
                        if you.handpoints() > dealer.handpoints():
                            if you.handpoints() == 21:
                                print("You win "+str(bet*3.0/2.0))
                                you.update_balance(bet*3.0/2.0) 
                            else:
                                print("You win "+str(bet))
                                you.update_balance(bet)
                        elif you.handpoints()==dealer.handpoints():
                            print("Tie! no money Lost") 
                        else:
                            you.update_balance(-bet)
                            print("House Wins! better luck next time")

                else:
                    you.update_balance(-bet)
                    print("House Wins! better luck next time")
            
            if you.balance > 0:
                play=input("Play Again? y,n")
            else:
                print("Not Enough money to play...")
                play='n'

    
    #read each deck. x is a string corresponding to a number between 1 and 100
#https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
    def ReadDeck(x):
        lines = [line.rstrip('\n') for line in open('/home/psimoesSsimoes/Github/trabalhojoana/baralhos/baralho_'+x+'.txt')]
        return lines

