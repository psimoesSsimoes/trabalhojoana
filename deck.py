#!python3.6i
#Importing the libraries
from collections import deque
from card import Card

class Deck:
    
    #constructor receives lines saved in a list and uses them to create a queue of object Card using it's own function create_deck
    def __init__(self,alist):
        self.deck = self.create_deck(alist)
    
    #https://www.pythoncentral.io/use-queue-beginners-guide/
    def create_deck(self,alist):
        queue = deque([])
        for line in alist:
            #split by space " "
            #https://www.tutorialspoint.com/python/string_split.html
            acard = line.split( )
            #create card object using values in list acard and function suite_to_number 
            queue.append(Card(acard[0],self.suite_to_number(acard[1])))
        return queue
        
    #https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
    #i don't really like this solution but i'm on a hurry
    #to represent suit we need a number corresponding to unicode symbol. so we use a dictionary to do that
    def suite_to_number(self,x):
        return {
            'E': 1,
            'C': 2,
            'P': 4,
            'O': 3,
        }[x]
    
    def popfromdeck(self):
        return self.deck.popleft() 
