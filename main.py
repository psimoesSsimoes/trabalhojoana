#!python3.6
#coding: utf8

def print_ronda(resultado,saldo,frase):
    print
    print("Resultado da ronda: "+frase+" com ganho "+str(float(resultado)))
    print("O seu saldo actual é: "+str(float(saldo)))

def handpoints(hand):
        points=0
        for i in hand:
            if i.split(" ")[0]=='A' and points+11 > 21:
                points+=1
            elif i.split(" ")[0]=='A' and points+11 <=21:
                points+=11
            elif i.split(" ")[0]=='K' or i.split(" ")[0]=='J' or i.split(" ")[0]=='Q':
                points+=10
            else:
                points+=int(i.split(" ")[0])
        
        return points

def show_deck(hand):
    s=""
    for i in hand:
        s+="("+i.replace(" ",",")+") "
    return s

def blackjack(points):
    return points == 21

def bust(points):
    return points > 21

#decision dealer
def ask_card(points):
    if points < 17:
        return True
    else: 
        return False

  #read each deck. x is a string corresponding to a number between 1 and 100
#https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
def ReadFile(x):
    lines = [line.rstrip('\n') for line in open('/home/psimoesSsimoes/Github/trabalhojoana/baralhos/baralho_'+x+'.txt')]
    return lines

# tuplo jogador guarda na posicao 0 nome, posicao 1 amount, posicao 2 bet
player=[]

name=raw_input("Nome do jogador?")

player.insert(0,name)
try:
    amount= int(raw_input("Montante inicial (100)?"))
except ValueError:
    amount=100.0

player.insert(1,amount)
try:
    bet=int(raw_input("Valor da aposta(10)?"))
except ValueError:
    bet=10.0

player.insert(2,bet)


rule=raw_input("Qual a regra do casino (s17 ou h17)?")


print
print("=== Vamos começar ===")
print("Jogador: "+ str(player[0]))
print("Saldo inicial: "+str(player[1]))
print("Valor da aposta: "+str(player[2]))
print

safe_word='palavra qualquer'
ronda=1
playerhand=[]
dealerhand=[]
dealer_points=0
player_points=0
option=""

while safe_word.lower()!="quit" and amount >= bet:
    print("*** Ronda "+str(ronda)+" ***")
    deck=ReadFile(str(ronda))
    for i in range(0,2):
        playerhand.append(deck.pop(0))
        dealerhand.append(deck.pop(0))
    
    print("Dealer: ("+dealerhand[0].replace(" ",",")+") (?,?)")
    
    #guardamos os pontos do player e do dealer
    dealer_points+=handpoints(dealerhand)
    player_points+=handpoints(playerhand)
    print("Jogador:("+playerhand[0].replace(" ",",")+") ("+playerhand[1].replace(" ",",")+")" +" - "+str(player_points)+" -")
    print
        

    print("* Joga "+str(player[0])+" *")
    
    if blackjack(player_points) and  not blackjack(dealer_points):
        
        print(str(player[0]) +" fez BLACKJACK!")
         
        player[1]+= 3 * player[2]/2


        
    else:

        while option.lower()!="stand":
            option = raw_input("HIT, STAND ou HINT ?")
            
            if option.lower()!="stand":
                print(str(player[0])+" decidiu HIT")
                
                playerhand.append(deck.pop(0))
                
                player_points=handpoints(playerhand)
                
                if bust(player_points):
                    print("BUST com "+str(player_points)+"pontos")
                    
                    player[1]-=player[2]
                
                    print_ronda(-player[2],player[1],"derrota com ganho")
                    
                    option="stand"

                    safe_word=raw_input("Mais uma ronda (QUIT para terminar)?")
                    print
                else:
                    print(show_deck(playerhand)+" -"+str(player_points)+" -") 
        
            else:
                print(str(player[0])+" decidiu STAND")
                print
        ####################### dealer plays ###################
        if not bust(player_points):
            print("* Joga o dealer *") 
            print("Mao dealer:")
            
            print(show_deck(dealerhand)+" -"+str(dealer_points)+" -") 
            
            if not blackjack(player_points) and blackjack(dealer_points):
                
                print("Dealer fez BLACKJACK!")
            
                player[1]-=player[2]
            
                
            elif not ask_card(dealer_points):
                print("Dealer decidiu STAND")

            else:
                
                #enquanto o dealer puder, pede cartas
                while ask_card(dealer_points):
                    
                    print("Dealer decidiu HIT")
                    
                    dealerhand.append(deck.pop(0))

                    # se o dealer rebenta
                    dealer_points=handpoints(dealer_hand)
                    
                    if bust(dealer_points):
                        
                        print("Mao dealer:")
                        
                        print(show_deck(dealer_hand)+" -"+str(dealer_points)+" -") 
                        
                        print("BUST com "+str(dealer_points)+" pontos")
                    else:
                        print("Mao dealer:")
                        
                        print(show_deck(dealer_hand)+" -"+str(dealer_points)+" -") 

                        if not ask_card(dealer_points):
                            print("Dealer decidiu STAND")
                
    #decisão de quem ganha
    if not bust(dealer_points) and not bust(player_points):
        if blackjack(player_points):
            
            print_ronda(3*player[2]/2,player[1],"vitória Blackjack")
            print 
        elif dealer_points > player_points:
            player[1]-=player[2]
            
            print_ronda(-player[2],player[1],"derrota com ganho")
            print         

                
        elif dealer_points==player_points:
                    
            print_ronda(0,player[1],"empate com ganho")
            print 
        else:
            print_ronda(player[2],player[1],"vitória com ganho")
                    
            safe_word=raw_input("Mais uma ronda (QUIT para terminar)?")
            print
              
    #voltar ao estado inicial
    print("atum")
    playerhand=[]
    
    dealerhand=[]
    
    dealer_points=0
    
    player_points=0
    
    option="uma palavra qq"
    #próxima ronda
    ronda+=1

# baralho = ReadDeck()



# p=Player(name,amount,bet,[])

# d=Dealer([])

# g=Game(p,d)

# g.play()

# g.showstats()

