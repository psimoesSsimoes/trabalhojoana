#!python3.6
#coding: utf8

from card import Card
from deck import Deck
#read each deck. x is a string corresponding to a number between 1 and 100
#https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
def ReadDeck(x):
    lines = [line.rstrip('\n') for line in open('/home/psimoesSsimoes/Github/trabalhojoana/baralhos/baralho_'+x+'.txt')]
    return lines

x=Deck(ReadDeck(str(1)))
for i in range(0, 10):
    y=x.popfromdeck()
    y.fancy()
