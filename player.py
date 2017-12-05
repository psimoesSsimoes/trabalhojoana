#!python3.6


class Player:
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
        self.hand=0
    
    #no verification is being made for negative balance
    def update_balance(self,x):
        self.amount+=x
    #if balance >=10  player can play
    def can_play(self):
        return self.balance >= 10
    
    #player balance
    def balance(self):
        return self.amount
    #player hand in one game
    def hand(self):
        return self.hand

    def emptyhand(self):
        return self.hand
    
    def addtohand(self,v):
        self.hand+=v
