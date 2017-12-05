#!python3.6


class Dealer:
    def __init__(self,hand):
        self.hand = hand

    def emptyhand(self):
        del self.hand[:]

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
   
    
    def can_play(self):
        points=self.handpoints()
        if points == 21:
            return False
        elif points > 21:
            return False
        elif points >=17:
            return False
        else:
            return True

    def showgame(self):
        print("DEALER's HAND:")
        for i in range(0, len(self.hand)-1):
            i.fancy()

