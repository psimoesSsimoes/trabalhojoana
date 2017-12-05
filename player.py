#!python3.6


class Player:
    def __init__(self,name,amount,bet,hand):
        self.name = name
        self.amount = amount
        self.bet=bet
        self.hand=hand
    
    #no verification is being made for when balance reaches negative state.
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
    
    #https://stackoverflow.com/questions/1400608/how-to-empty-a-list-in-python
    def emptyhand(self):
        del self.hand[:]
    
    #add card to hand
    def addtohand(self,v):
        self.hand.append(v)
    
    #calculate points
    def handpoints(self):
        points=0
        for i in self.hand:
            if i.value()=='A' && points+11 > 21:
                points+=1
            elif i.value()=='A' && points+11 <=21:
                points+=11
            elif i.value()=='K' || i.value()=='J' || i.value()=='Q':
                points+=10
            else:
                points+=int(i.value())
        
        return points
    #show hand 
    

    def showhand(self):
        for i in self.hand:
            h+=i.normal()+" "
        return h

    def betvalue(self):
        return self.bet

    def pprint(self):
        print("Jogador: "+str(name))
        print("Saldo Inicial: "+str(amount))
        print("Valor da aposta: "+str(bet))
    
    def whoplays(self):
        return "* Joga "+self.name+" *"
    
    def blackjack(self):
        return self.name+" fez BLACKJACK!"
