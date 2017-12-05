#!python3.6


class Player:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.hand=0
    
    #no verification is being made for negative balance
    def update_balance(self,x):
        self.balance+=x
    #if balance >=10  player can play
    def can_play(self):
        return self.balance >= 10
    
    #player balance
    def balance(self):
        return self.balance
    #player hand in one game
    def hand(self):
        return self.hand

    def emptyhand(self):
        return self.hand
    
    def addtohand(self,v)
        self.hand+v
