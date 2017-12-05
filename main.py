#!python3.6
#coding: utf8

from card import Card
from deck import Deck
from player import Player




#read each deck. x is a string corresponding to a number between 1 and 100
#https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
def ReadDeck(x):
    lines = [line.rstrip('\n') for line in open('/home/psimoesSsimoes/Github/trabalhojoana/baralhos/baralho_'+x+'.txt')]
    return lines

#two arrays of cards, p of you, d of dealer
def showgame(p,d):
    print("YOUR HAND:")
    for i in p:
        i.fancy()
    
    print("DEALER'S HAND:")
    d[0].fancy() 






name = raw_input("Name?")

#https://docs.python.org/2/tutorial/errors.html
try:
    amount= float(raw_input("Amount?"))
except ValueError:
    amount=100.0

print("Welcome to the wonderfull world of blackjack "+name+"!")
print("Your initial amount is "+str(amount))
print("Have a great game!")

you=Player(name,amount)

#a flag to know when to exit the game
exit=0
which_deck=1

while you.can_play() and exit==0:
    try:
        bet=float(raw_input("how much you want to bet?"))
        
        if bet > you.balance():
            bet=10.0 
    except ValueError:
        bet=10.0
    #player and dealer are just an array of Cards
    p=[]
    d=[]
    print("Bet of "+str(bet))
    deck=Deck(ReadDeck(str(which_deck)))
    #gives two cards
    for i in range(0,2):
        p.append(deck.popfromdeck())
        d.append(deck.popfromdeck())
    
    showgame(p,d)
    print("HIT OR STAND?")

# for i in range(0, 10):
#     y=x.popfromdeck()
#     y.fancy()
