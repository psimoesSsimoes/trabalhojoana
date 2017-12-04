#!python3.6
#coding: utf8
class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = u'\u2660\u2661\u2662\u2663'[suit-1]   # 1,2,3,4 = ♥♦♣♠

    def fancy(self):
        print(self.suit)
        print("┌───────┐")
        print("| {:<2}    |".format(self.value))
        print("|       |")
        print("|   "+self.suit + "   |")
        print("|       |")
        print("|    {:>2} |".format(self.value))
        print("└───────┘")
