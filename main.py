#!python3.6
#coding: utf8

from card import Card
from deck import Deck
from player import Player





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


# for i in range(0, 10):
#     y=x.popfromdeck()
#     y.fancy()
