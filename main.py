#!python3.6
#coding: utf8

from card import Card
from deck import Deck
from player import Player
from game import Game

name=input("Nome do jogador?")

try:
    amount= float(raw_input("Montante inicial (100)?"))
except ValueError:
    amount=100.0

try:
    bet=float(input("Valor da aposta(10)?"))
except ValueError:
    bet=10

if bet > amount:
    #wtf happens? ask the teacher

rule=input("Qual a regra do casino (s17 ou h17)?")

p=Player(name,amount,bet,[])

d=Dealer([])

g=Game(p,d)

g.play()

g.showstats()

