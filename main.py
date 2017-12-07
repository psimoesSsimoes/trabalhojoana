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

def stats(player_name,rounds,inicial_amount,final_amount,wins,losses,ties,nblack):
    print
    print("=== Algumas estatísticas ===")
    print(str(player_name)+" jogou "+str(rounds)+ " rondas.")
    print("Entrou no jogo com "+str(inicial_amount)+ " e agora tem "+str(final_amount))
    print("número de vitórias: "+str(wins))
    print("número de derrotas: "+str(losses))
    print("número de empates: "+str(ties))
    print("vitórias blackjack: "+str(nblack))

#se tem às,então retorna false. A verificação dos 17 pontos é feita em baixo
def soft(hand):
    for i in hand:
        if i.split(" ")[0]=='A':
            return False
    return True

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
def ask_card(points,mode):
    if points < 17 and mode=="s17":
        return True
    elif points >=17 and mode=="s17":
        return False 
    elif points <=17:
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

if rule.lower()!="h17":
    rule="s17"
else:
    rule=rule.lower()

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
inicial_amount=player[1]
wins=0
losses=0
ties=0
nblack=0
seventeen=False
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
        wins+=1
        nblackjack+=1
        


    elif blackjack(player_points) and blackjack(dealer_points):
        
        print(str(player[0]) +" fez BLACKJACK!")
        print("* Joga o dealer *") 
        print("Mao dealer:")
        print(show_deck(dealerhand)+" -"+str(dealer_points)+" -") 
        print("Dealer fez BLACKJACK!")
        print
        ties+=1

    else:

        while option.lower()!="stand":
            option = raw_input("HIT, STAND ou HINT ?")
            
            if option.lower()!="stand":
                print(str(player[0])+" decidiu HIT")
                
                playerhand.append(deck.pop(0))
                
                player_points=handpoints(playerhand)
                
                if bust(player_points):
                    print("BUST com "+str(player_points)+" pontos")
                    
                    player[1]-=player[2]
                
                    print_ronda(-player[2],player[1],"derrota com ganho")
                    
                    option="stand"
                    losses+=1

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
                losses+=1
                
            elif not ask_card(dealer_points,rule):
                print("Dealer decidiu STAND")

            else:
                
                #enquanto o dealer puder, pede cartas
                while ask_card(dealer_points,rule):
                    
                    print("Dealer decidiu HIT")
                    
                    dealerhand.append(deck.pop(0))
                    
                    dealer_points=handpoints(dealerhand)

                    if bust(dealer_points):
                        
                        print("Mao dealer:")
                        
                        print(show_deck(dealerhand)+" -"+str(dealer_points)+" -") 
                        
                        print("BUST com "+str(dealer_points)+" pontos")
                        wins+=1
                        player[1]+=player[2]

                        print_ronda(player[2],player[1],"vitória com ganho")

                        safe_word=raw_input("Mais uma ronda (QUIT para terminar)?")
                        print

                    else:
                        print("Mao dealer:")
                        
                        print(show_deck(dealerhand)+" -"+str(dealer_points)+" -") 

                        if not ask_card(dealer_points,rule):
                            print("Dealer decidiu STAND")
                
    #decisão de quem ganha
    if not bust(dealer_points) and not bust(player_points):
        
        if blackjack(player_points) and blackjack(dealer_points):
            print_ronda(0,player[1],"empate com ganho")
            ties+=1
            safe_word=raw_input("Mais uma ronda (QUIT para terminar)?")
            print

        
        elif blackjack(player_points):
            
            print_ronda(3*player[2]/2,player[1],"vitória Blackjack")
            wins+=1
            nblackjack+=1
            safe_word=raw_input("Mais uma ronda (QUIT para terminar)?")
            print 
        
        elif blackjack(dealer_points):
            print_ronda(-player[2],player[1],"derrota com ganho")
            losses+=1
            safe_word=raw_input("Mais uma ronda (QUIT para terminar)?")
            print 

        elif dealer_points > player_points:
            player[1]-=player[2]
            
            print_ronda(-player[2],player[1],"derrota com ganho")
            losses+=1
            safe_word=raw_input("Mais uma ronda (QUIT para terminar)?")
            print


                
        elif dealer_points==player_points:
                    
            print_ronda(0,player[1],"empate com ganho")
            ties+=1
            safe_word=raw_input("Mais uma ronda (QUIT para terminar)?")
            print

        else:
            player[1]+=player[2]
            print_ronda(player[2],player[1],"vitória com ganho")
            wins+=1        
            safe_word=raw_input("Mais uma ronda (QUIT para terminar)?")
            print
              
    #voltar ao estado inicial
    playerhand=[]
    
    dealerhand=[]
    
    dealer_points=0
    
    player_points=0
    
    option="uma palavra qq"
    #próxima ronda
    ronda+=1


stats(player[0],ronda-1,inicial_amount,player[1],wins,losses,ties,nblack)
