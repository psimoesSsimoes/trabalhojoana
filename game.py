#!python3.6
#coding: utf8

from card import Card
from deck import Deck
from player import Player

class Game:
    
    def __init__(self,player):
        self.you=player


    def play(self):
        while you.can_play() and exit==0:
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
                p.append(deck.popfromdeck())
                d.append(deck.popfromdeck())
    
            showgame(p,d)
            print("HIT OR STAND?")

    
    
    #read each deck. x is a string corresponding to a number between 1 and 100
#https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
    def ReadDeck(x):
        lines = [line.rstrip('\n') for line in open('/home/psimoesSsimoes/Github/trabalhojoana/baralhos/baralho_'+x+'.txt')]
        return lines

