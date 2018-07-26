import random

#play=[10,20,50,60]
play=[None]*4
#hand = list("")
#hand=[1,2,3,23,44,66,80,90]
hand=list("")
options=list("")
deck = list("")
option_enum=list("")
for i in range(1,99):
        deck.append(i)
random.shuffle(deck)
#print(deck)
#print(deck.pop())

def initialize():
        #play = ["none"]*4
        #hand = ["none"]*8
        #print(deck)
        for i in range(8):
                hand.append(deck.pop())
                options.append(0)
                #print("Popped "+str(hand[i]))

def available_options():
        option_enum=list("")
        for i in range(len(hand)):
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
        print("Enumerated options are"+ str(option_enum))
        return sum(options)

def simpleprint():
        print("Cards in Play zone"+str(play))
        print("Cards in Hand zone"+str(hand))
        print("Options for Hand"+str(options))

def validoption(choise):
        handindex = choise//10
        playindex = choise%10
        if(play[playindex]==None):return True
        elif((playindex==0 or playindex==1) and (hand[handindex]>play[playindex] or hand[handindex]==(play[playindex]-10))):return True
        elif((playindex==2 or playindex==3) and (hand[handindex]<play[playindex] or hand[handindex]==(play[playindex]+10))):return True
        else: return False

def choose():
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
                choose()
        #End game if no options are available
        if(available_options()==0):
                print("Game over")
                return
        print("State after choosing Hand position : "+ str(handindex) +" Play position : "+ str(playindex))
        simpleprint()
        count = available_options()
def draw():
        pop_number = deck.pop()
        hand.append(pop_number)
        print("Added "+str(pop_number)+" to the hand")
        pop_number = deck.pop()
        hand.append(pop_number)
        print("Added "+str(pop_number)+" to the hand")
        print("Hand after draw")
        simpleprint()

initialize()
count = available_options()
simpleprint()
while(available_options()):
        choose()
        choose()
        draw()
