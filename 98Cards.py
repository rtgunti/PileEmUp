import random
deck = list("")         #Deck has shuffeled cards numbered from 2 to 98
for i in range(2,99):
        deck.append(i)
random.shuffle(deck)
hand=list("")           #Hand Zone has 8 slots. Cards are drawn from deck and placed in Hand Zone
play=[None]*4           #Play Zone. Cards drawn from hand are placed on board. Game starts with 4 empty slots
options=list("")        #A list to save how many options each card from Hand Zone has. 
option_enum=list("")    #Ennumberation of all available options. Ex: int((10*x)+y) x is hand index and y is play index

#print(deck)
#print(deck.pop())

def initialize():
        #play = ["none"]*4
        #hand = ["none"]*8
        #print(deck)
        for i in range(8):
                hand.append(deck.pop())         #Pop cards from deck and place in hand
                options.append(4)               #At the beginning of the game, every card in hand has 4 options. 
                #print("Popped "+str(hand[i]))

def available_options():                        
        option_enum=list("")                    #Reset the enum list every time

        for i in range(len(hand)):              #Reset options counter to zero
                options[i]=0
        for i in hand:
                #print("Available options for "+str(i)+" card are ")
                if(play[0]==None or i>play[0] or i==(play[0]-10)): 
                        options[hand.index(i)]+=1
                        option_enum.append(hand.index(i)*10+0)
                        #print("Card "+str(i)+" can be placed in position 0")
                if(play[1]==None or i>play[1] or i==(play[1]-10)): 
                        options[hand.index(i)]+=1
                        option_enum.append(hand.index(i)*10+1)
                        #print("Card "+str(i)+" can be placed in position 1")
                if(play[2]==None or i<play[2] or i==(play[2]+10)):
                        options[hand.index(i)]+=1
                        option_enum.append(hand.index(i)*10+2)
                        #print("Card "+str(i)+" can be placed in position 2")
                if(play[3]==None or i<play[3] or i==(play[3]+10)):
                        options[hand.index(i)]+=1
                        option_enum.append(hand.index(i)*10+3)
                        #print("Card "+str(i)+" can be placed in position 3")
        return option_enum

def simpleprint():
        print("Cards in Play zone")
        print(str(play))
        print("Cards in Hand zone")
        print(str(hand))
        print("Options for each card in Hand")
        print(str(options))
        print("Number of options : ")
        print(str(len(available_options())))
        print("Available options are")
        print(str(available_options()))

def validoption(choise):
        handindex = choise//10
        playindex = choise%10
        if(handindex>7 or playindex>3): return False
        elif(play[playindex]==None):return True
        elif((playindex==0 or playindex==1) and (hand[handindex]>play[playindex] or hand[handindex]==(play[playindex]-10))):return True
        elif((playindex==2 or playindex==3) and (hand[handindex]<play[playindex] or hand[handindex]==(play[playindex]+10))):return True
        else: return False

def choose():
        #End game if no options are available
        if(len(available_options())==0):
                return
        choise = int(input('Enter index of handzone and playzone: '))
        handindex = choise//10
        playindex = choise%10
        # try:
        #         mode=int(raw_input('Input:'))
        # except ValueError:
        #         print ("Not a number") 
        if(validoption(choise)):
                play[playindex]=hand[handindex]
                options.remove(options[handindex])
                hand.remove(hand[handindex])
        else:
                print("Invalid option. Choose again")
                return
        #print("State after choosing Hand position : "+ str(handindex) +" Play position : "+ str(playindex))
        #simpleprint()

def chooserandom():
        #choise = random.choises(deck)
        choises = available_options()
        if(len(choises)==0):
                return
        rand_item = choises[random.randrange(len(choises))]
        print("Random option "+str(rand_item)+" choosen")
        handindex = rand_item//10
        playindex = rand_item%10
        play[playindex]=hand[handindex]
        options.remove(options[handindex])
        hand.remove(hand[handindex])


def draw():
        pop_number = deck.pop()
        hand.append(pop_number)
        options.append(0)
        print("Added "+str(pop_number)+" to the hand")
        pop_number = deck.pop()
        hand.append(pop_number)
        options.append(0)
        print("Added "+str(pop_number)+" to the hand")
        #print("Hand after draw")
        #simpleprint()

initialize()
#count = available_options()
while(available_options()!=[]):
        if(len(hand)==6):draw()
        simpleprint()
        #choose()     		#Reads input from user
        chooserandom()		#Randomly chooses and available option
simpleprint()
print("Game over")
print("Score is "+str(98-len(deck)))
