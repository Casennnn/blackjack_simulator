import random, os, time, sys


class Deck():
    def __init__(self, numOfDeck):
        self.numOfDeck = numOfDeck
        self.suits = ['♠', '♣', '♥', '♦']
        self.ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.theDeck = []
        for _ in range(numOfDeck):
            self.appendDeck = [(rank, suit) for suit in self.suits for rank in self.ranks]
            self.theDeck += self.appendDeck

    def shuffleDeck(self):
        random.shuffle(self.theDeck)
        random.shuffle(self.theDeck)

dealingSpeed = 0.3
cont = True
while cont:
    cont = False
    try:
        numOfDeck = int(input("Enter the number of Decks you wanna play with: (1-10) "))
        auto = input("Autoplay or not? (y/n) ")
        if auto=="y":
            goalrate = float(input("Please input the initial betting size as a proportion of the balance. Suggest (0.001-0.02) "))
            isauto = True
            ishint = 'n'
            dealingSpeed += 0.3
        else:
            goalrate = 0
            ishint = input("Hint for action or not? (y/n) ")
            isauto = False

        startingbalance = 10000
    except:
        cont = True
instance = Deck(numOfDeck)
instance.shuffleDeck()
valueMap = {instance.ranks[i]:i+1 for i in range(13)}
valueMap['J'] = 10
valueMap['Q'] = 10
valueMap['K'] = 10



rounds = 0
wincount = 0
lasthandwin= True
unit = int(startingbalance*goalrate)  #goal is 0.5% for each session
lastbet = unit
goal = startingbalance + unit

#--------one round begin-----------
while True:
    if rounds>0:
        winrate = wincount/rounds
    else:
        winrate = 0
    if len(instance.theDeck)<20:
            #print("New Deck!")
            instance = Deck(numOfDeck)
            instance.shuffleDeck()
    iswin = False
    blackJack = False
    ispush = False
    os.system('cls')
    print("Balance: ", round(startingbalance, 1),  "\tCards left in the deck: ", len(instance.theDeck), "\tWinrate: ", round(winrate*100,3), "%")
    print("===========")
    print("Dealer: ")
    print("\n\n\n")
    print("Your hand: ")
    print("===========")
    if not isauto:
        cont = True
        while cont:
            cont = False
            try:
                bet = int(input("Please input your betting size: "))
                if startingbalance - bet <0:
                    print("Your balance is not enough, please enter again")
                    raise ValueError
            except:
                cont = True
    else:
        if not lasthandwin:
            bet = lastbet*2
        else:
            # if startingbalance<goal:
            #     # if startingbalance<=lastbet*5:
            #     #     unit = int(startingbalance/100)  #goal is 1% for each session
            #     #     lastbet = unit
            #     #     goal = startingbalance + unit
            #     #     bet = lastbet
            #     # else:
            #     bet += unit

            # else: #restart session
            unit = int(startingbalance*goalrate)  #goal is 0.5% for each session
            lastbet = unit
            goal = startingbalance + unit
            bet = lastbet
    print("Betsize now is: ", bet)
    time.sleep(1)
    lastbet = bet
    startingbalance -= bet
    if startingbalance <0:
        print("Your balance is not enough to execute the require bet according to the strategy, simulation ends!")
        wait= input()
        break

    time.sleep(0.2)

    yourCards = [instance.theDeck.pop(0)]
    dealerCards = [instance.theDeck.pop(0)]
    yourCards.append(instance.theDeck.pop(0))  #yourCards = [('A','suit'),('K','suit')]
    dealerCards.append(instance.theDeck.pop(0))  
    yourValue = valueMap[yourCards[0][0]] + valueMap[yourCards[1][0]]   
    dealerValue = valueMap[dealerCards[0][0]] + valueMap[dealerCards[1][0]]   

    os.system('cls')

    print("Balance: ", round(startingbalance, 1), "\tCards left in the deck: ", len(instance.theDeck)+3,  "\tWinrate: ", round(winrate*100,3), "%")
    print("===========")
    print("Dealer: ")
    print("\n\n\n")
    print("Your hand: ", yourCards[0][0]+yourCards[0][1])
    print("===========")
    time.sleep(dealingSpeed)

    os.system('cls')

    print("Balance: ", round(startingbalance, 1), "\tCards left in the deck: ", len(instance.theDeck)+2, "\tWinrate: ", round(winrate*100,3), "%")
    print("===========")
    print("Dealer: ",dealerCards[0][0]+dealerCards[0][1] )
    print("\n\n\n")
    print("Your hand: ", yourCards[0][0]+yourCards[0][1])
    print("===========")
    time.sleep(dealingSpeed)

    os.system('cls')

    print("Balance: ", round(startingbalance, 1), "\tCards left in the deck: ", len(instance.theDeck)+1, "\tWinrate: ", round(winrate*100,3), "%")
    print("===========")
    print("Dealer: ",dealerCards[0][0]+dealerCards[0][1] )
    print("\n\n\n")
    print("Your hand: ", yourCards[0][0]+yourCards[0][1], yourCards[1][0]+yourCards[1][1])
    print("===========")
    time.sleep(dealingSpeed)

    yourDisplayString = str(yourCards[0][0]+yourCards[0][1] + " " + yourCards[1][0]+yourCards[1][1])
    ace11 = False
    action = 'i'
    while action =='h' or action=='i':
        if action=="h":
            yourCards.append(instance.theDeck.pop(0)) 
            yourValue += valueMap[yourCards[-1][0]]
            yourDisplayString += " "+ yourCards[-1][0]+yourCards[-1][1]

        os.system('cls')
        if yourDisplayString.count('A') >0 and yourValue+10<=21:
            ace11 = True
            yourValue += 10

        print("Balance: ", round(startingbalance, 1), "\tCards left in the deck: ", len(instance.theDeck), "\tWinrate: ", round(winrate*100,3), "%")
        print("===========")
        print("Dealer: ",dealerCards[0][0]+dealerCards[0][1], " (Hidden)" )
        print("\n\n\n")
        print("Your hand: ", yourDisplayString)
        print("===========")

        if yourValue==21 and action == 'i':
            blackJack =True
            iswin = True
            break
        if yourValue>21 and not ace11:
            print("\nYou busted!! Dealer wins.")
            break
        elif yourValue>21 and ace11:
            ace11 = False
            yourValue -= 10   
        if yourValue==21:
            print("\nYou got 21!!.")  #can still be a push
            time.sleep(dealingSpeed+1)
            break

        if ace11:
            print("YourValue: ",yourValue-10,"/",yourValue )
        else:
            print("YourValue: ", yourValue)
        #print("DealerValue: ",dealerValue)
        print("\n")

        if yourValue<=11:
            if ishint == 'y':
                print('Hints: h')
            if isauto:
                action = 'h'
            else:
                action = input("Hit or Stand? (h/s)")
            
        else:
            if not ace11:
                if valueMap[dealerCards[0][0]]>=4 and valueMap[dealerCards[0][0]]<=6:
                    if ishint == 'y':
                        print('Hints: s')
                    if isauto:
                        action = 's'
                    else:
                        action = input("Hit or Stand? (h/s)")
                    
                elif yourValue==12:
                    if ishint == 'y':
                        print('Hints: h')
                    if isauto:
                        action = 'h'
                    else:
                        action = input("Hit or Stand? (h/s)")
                    
                elif valueMap[dealerCards[0][0]]<=6 and valueMap[dealerCards[0][0]]!=1:
                    if ishint == 'y':
                        print('Hints: s')
                    if isauto:
                        action = 's'
                    else:
                        action = input("Hit or Stand? (h/s)")
                    
                elif yourValue<=16:
                    if ishint == 'y':
                        print('Hints: h')
                    if isauto:
                        action = 'h'
                    else:
                        action = input("Hit or Stand? (h/s)")
                    
                else:
                    if ishint == 'y':
                        print('Hints: s')
                    if isauto:
                        action = 's'
                    else:
                        action = input("Hit or Stand? (h/s)")
                
            else:
                if yourValue<=17:
                    if ishint == 'y':
                        print('Hints: h')
                    if isauto:
                        action = 'h'
                    else:
                        action = input("Hit or Stand? (h/s)")
                    
                elif yourValue >=19:
                    if ishint == 'y':
                        print('Hints: s')
                    if isauto:
                        action = 's'
                    else:
                        action = input("Hit or Stand? (h/s)")
                    
                elif valueMap[dealerCards[0][0]]<=8 and valueMap[dealerCards[0][0]]!=1:
                    if ishint == 'y':
                        print('Hints: s')
                    if isauto:
                        action = 's'
                    else:
                        action = input("Hit or Stand? (h/s)")
                    
                else:
                    if ishint == 'y':
                        print('Hints: h')
                    if isauto:
                        action = 'h'
                    else:
                        action = input("Hit or Stand? (h/s)")


        #action = input("Hit or Stand? (h/s)")


        while action != 'h' and action !='s':
            print("Invalid Input! Try again")
            action = input("Hit or Stand? (h/s)")
        time.sleep(dealingSpeed)

    if yourValue>21:
        isBusted = True
    else:
        isBusted = False

    if not isBusted and not blackJack:
        #dealer have to hit
        dealerDisplayString = str(dealerCards[0][0]+dealerCards[0][1] + " "+ dealerCards[1][0]+dealerCards[1][1])
        dealerace11 = False
        if dealerDisplayString.count('A') >0 and dealerValue+10<=21:
            dealerace11 = True
            dealerValue += 10

        os.system('cls')
        print("Balance: ", round(startingbalance, 1), "\tCards left in the deck: ", len(instance.theDeck), "\tWinrate: ", round(winrate*100,3), "%")
        print("===========")
        print("Dealer: ",dealerDisplayString )
        print("\n\n\n")
        print("Your hand: ", yourDisplayString)
        print("===========")
        print("DealerValue: ",dealerValue)
        print("YourValue: ",yourValue)
        time.sleep(dealingSpeed+1)
        while dealerValue<17:

            dealerCards.append(instance.theDeck.pop(0)) 
            dealerValue += valueMap[dealerCards[-1][0]]
            dealerDisplayString += " "+ dealerCards[-1][0]+dealerCards[-1][1]
            
            if dealerDisplayString.count('A') >0 and dealerValue+10<=21:
                dealerace11 = True
                dealerValue += 10

            os.system('cls')
            print("Balance: ", round(startingbalance, 1), "\tCards left in the deck: ", len(instance.theDeck), "\tWinrate: ", round(winrate*100,3), "%")
            print("===========")
            print("Dealer: ",dealerDisplayString )
            print("\n\n\n")
            print("Your hand: ", yourDisplayString)
            print("===========")

            if dealerValue>21 and dealerace11:
                dealerace11 = False
                dealerValue -= 10
            print("DealerValue: ",dealerValue)
            print("YourValue: ", yourValue)
            
            if dealerValue ==21:
                break

            
            if dealerValue>21 and not dealerace11:
                print("\nDealer busted!!")
                iswin = True
                break
            time.sleep(dealingSpeed+1)


    if yourValue==dealerValue:
        ispush= True
    elif yourValue>dealerValue and not isBusted:
        iswin = True

    if iswin:
        wincount+=1
        lasthandwin = True
    else:
        lasthandwin = False
    rounds +=1
    if iswin and blackJack:
        startingbalance += int(bet*2.5)
        print("\nCongratulations!! You got BlackJack!")
    if iswin and not blackJack:
        startingbalance += bet *2
        print("\nYou win!")
    if ispush and dealerValue==21:
        startingbalance += bet
        print("\nDealer also got 21! Push!")
    elif ispush:
        startingbalance += bet
        print("\nIt is a push!")
    
    if not iswin and not isBusted and not ispush:
        print("\nYou lose!")

    if not isauto:
        if iswin:
            wait = input("\nPress Enter to collect ur winning and start next round...")
        else:
            wait = input("\nPress Enter to start next round...")
    else:
        time.sleep(dealingSpeed)


#--------one round end-----------


