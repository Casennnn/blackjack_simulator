import random, os, time, sys, statistics, math
from tqdm import tqdm
import matplotlib.pyplot as plt

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




dealingSpeed = 0

numOfDeck = int(input("Please enter the number of deck used in simulation:\n"))
# accuracy = int(input("Please enter the level of accuracy used in simulation:(1 to 20, where 50 will take some time with higher accuracy)\n"))
numofGambler = int(input("Please enter the number of gamblers used in simulation:(100 to 2000, where 2000 will take some time with higher accuracy)\n"))
graph = int(input("please state whether you want to output the result graph of winrate_vs_sharpe or not. Yes(1)/No(0)\n"))
goalrate = min(max(float(input("Please enter the initial betting initial as a proportion of the initial balance. Suggestion: 0.0001 - 0.5\n")), 0), 1)

isauto = True
instance = Deck(numOfDeck)
instance.shuffleDeck()
valueMap = {instance.ranks[i]:i+1 for i in range(13)}
valueMap['J'] = 10
valueMap['Q'] = 10
valueMap['K'] = 10



listOfSharpe = []
listOfwinrate = []
listOfgoalrate = []
listOfNumofHand =[]



dictofdifftrial = []
rreturn = []
#goalrate = 0.01/2

#numofHands = 50
accuracy = 3

maxwinrate = 0
# for i in tqdm(range(1,101)):
# goalrate =  0.0001
#for i in tqdm(range(1,40)):
# numofHands = 13

for _ in tqdm(range(accuracy)):
    
    for numofHands in tqdm(range(7,51)):
        for i in range(numofGambler):
        #--------one round begin-----------
            startingbalance = 10000
            initialbalance = startingbalance
            rounds = 0
            wincount = 0
            lasthandwin= False
            unit = int(startingbalance*goalrate)  #goal is 1% for each session
            lastbet = unit
            goal = startingbalance + unit
            # balancechange = []
            ispush = False
            while startingbalance>=unit and rounds<=numofHands:
                # balancechange.append(startingbalance)
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
                # os.system('cls')
                # print("Balance: ", round(startingbalance, 1),  "\tCards left in the deck: ", len(instance.theDeck), "\tWinrate: ", round(winrate*100,3), "%")
                # print("===========")
                # print("Dealer: ")
                # print("\n\n\n")
                # print("Your hand: ")
                # print("===========")
                if not isauto:
                    cont = True
                    while cont:
                        cont = False
                        try:
                            bet = int(input("Please input your betting size: "))
                        except:
                            cont = True
                else:
                    if not lasthandwin and not ispush:
                        bet = lastbet*2
                    else:
                        if ispush:
                            bet = lastbet
                        else:
                            bet = unit
                ispush = False
                # print("Betsize now is: ", bet)s
                # time.sleep(1)
                lastbet = bet
                if (startingbalance-bet) <0:
                    bet = startingbalance
                    #print("Your balance is not enough, please enter again")
                    #startingbalance+=bet
                    # rounds+=1
                    # continue
                if startingbalance ==0:
                    rounds +=1
                    continue

                #bet = int(startingbalance/100)
                startingbalance -= bet

                #time.sleep(0.2)

                yourCards = [instance.theDeck.pop(0)]
                dealerCards = [instance.theDeck.pop(0)]
                yourCards.append(instance.theDeck.pop(0))  #yourCards = [('A','suit'),('K','suit')]
                dealerCards.append(instance.theDeck.pop(0))  
                yourValue = valueMap[yourCards[0][0]] + valueMap[yourCards[1][0]]   
                dealerValue = valueMap[dealerCards[0][0]] + valueMap[dealerCards[1][0]]   

                # os.system('cls')

                # print("Balance: ", round(startingbalance, 1), "\tCards left in the deck: ", len(instance.theDeck)+3,  "\tWinrate: ", round(winrate*100,3), "%")
                # print("===========")
                # print("Dealer: ")
                # print("\n\n\n")
                # print("Your hand: ", yourCards[0][0]+yourCards[0][1])
                # print("===========")
                # time.sleep(dealingSpeed)

                # os.system('cls')

                # print("Balance: ", round(startingbalance, 1), "\tCards left in the deck: ", len(instance.theDeck)+2, "\tWinrate: ", round(winrate*100,3), "%")
                # print("===========")
                # print("Dealer: ",dealerCards[0][0]+dealerCards[0][1] )
                # print("\n\n\n")
                # print("Your hand: ", yourCards[0][0]+yourCards[0][1])
                # print("===========")
                # time.sleep(dealingSpeed)

                # os.system('cls')

                # print("Balance: ", round(startingbalance, 1), "\tCards left in the deck: ", len(instance.theDeck)+1, "\tWinrate: ", round(winrate*100,3), "%")
                # print("===========")
                # print("Dealer: ",dealerCards[0][0]+dealerCards[0][1] )
                # print("\n\n\n")
                # print("Your hand: ", yourCards[0][0]+yourCards[0][1], yourCards[1][0]+yourCards[1][1])
                # print("===========")
                # time.sleep(dealingSpeed)

                yourDisplayString = str(yourCards[0][0]+yourCards[0][1] + " " + yourCards[1][0]+yourCards[1][1])
                ace11 = False
                action = 'i'
                while action =='h' or action=='i':
                    if action=="h":
                        yourCards.append(instance.theDeck.pop(0)) 
                        yourValue += valueMap[yourCards[-1][0]]
                        yourDisplayString += " "+ yourCards[-1][0]+yourCards[-1][1]

                    #os.system('cls')
                    if yourDisplayString.count('A') >0 and yourValue+10<=21:
                        ace11 = True
                        yourValue += 10

                    # print("Balance: ", round(startingbalance, 1), "\tCards left in the deck: ", len(instance.theDeck), "\tWinrate: ", round(winrate*100,3), "%")
                    # print("===========")
                    # print("Dealer: ",dealerCards[0][0]+dealerCards[0][1], " (Hidden)" )
                    # print("\n\n\n")
                    # print("Your hand: ", yourDisplayString)
                    # print("===========")

                    if yourValue==21 and action == 'i':
                        blackJack =True
                        iswin = True
                        break
                    if yourValue>21 and not ace11:
                        #print("\nYou busted!! Dealer wins.")
                        break
                    elif yourValue>21 and ace11:
                        ace11 = False
                        yourValue -= 10   
                    if yourValue==21:
                        #print("\nYou got 21!!.")  #can still be a push
                        #time.sleep(dealingSpeed+1)
                        break

                    # if ace11:
                    #     #print("YourValue: ",yourValue-10,"/",yourValue )
                    # else:
                        #print("YourValue: ", yourValue)
                    #print("DealerValue: ",dealerValue)
                    #print("\n")

                    if yourValue<=11:
                        #print('Hints: h')
                        if isauto:
                            action = 'h'
                        else:
                            action = input("Hit or Stand? (h/s)")
                        
                    else:
                        # action = 's'
                        # continue
                        if not ace11:
                            if valueMap[dealerCards[0][0]]>=4 and valueMap[dealerCards[0][0]]<=6:
                                #print('Hints: s')
                                if isauto:
                                    action = 's'
                                else:
                                    action = input("Hit or Stand? (h/s)")
                                
                            elif yourValue==12:
                                #print('Hints: h')
                                if isauto:
                                    action = 'h'
                                else:
                                    action = input("Hit or Stand? (h/s)")
                                
                            elif valueMap[dealerCards[0][0]]<=6 and valueMap[dealerCards[0][0]]!=1:
                                #print('Hints: s')
                                if isauto:
                                    action = 's'
                                else:
                                    action = input("Hit or Stand? (h/s)")
                                
                            elif yourValue<=16:
                                #print('Hints: h')
                                if isauto:
                                    action = 'h'
                                else:
                                    action = input("Hit or Stand? (h/s)")
                                
                            else:
                                #print('Hints: s')
                                if isauto:
                                    action = 's'
                                else:
                                    action = input("Hit or Stand? (h/s)")
                            
                        else:
                            if yourValue<=17:
                                #print('Hints: h')
                                if isauto:
                                    action = 'h'
                                else:
                                    action = input("Hit or Stand? (h/s)")
                                
                            elif yourValue >=19:
                                #print('Hints: s')
                                if isauto:
                                    action = 's'
                                else:
                                    action = input("Hit or Stand? (h/s)")
                                
                            elif valueMap[dealerCards[0][0]]<=8 and valueMap[dealerCards[0][0]]!=1:
                                #print('Hints: s')
                                if isauto:
                                    action = 's'
                                else:
                                    action = input("Hit or Stand? (h/s)")
                                
                            else:
                                #print('Hints: h')
                                if isauto:
                                    action = 'h'
                                else:
                                    action = input("Hit or Stand? (h/s)")


                    #action = input("Hit or Stand? (h/s)")


                    while action != 'h' and action !='s':
                        print("Invalid Input! Try again")
                        action = input("Hit or Stand? (h/s)")
                    #time.sleep(dealingSpeed)

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

                    # os.system('cls')
                    # print("Balance: ", round(startingbalance, 1), "\tCards left in the deck: ", len(instance.theDeck), "\tWinrate: ", round(winrate*100,3), "%")
                    # print("===========")
                    # print("Dealer: ",dealerDisplayString )
                    # print("\n\n\n")
                    # print("Your hand: ", yourDisplayString)
                    # print("===========")
                    # print("DealerValue: ",dealerValue)
                    # print("YourValue: ",yourValue)
                    # time.sleep(dealingSpeed+1)
                    while dealerValue<17:

                        dealerCards.append(instance.theDeck.pop(0)) 
                        dealerValue += valueMap[dealerCards[-1][0]]
                        dealerDisplayString += " "+ dealerCards[-1][0]+dealerCards[-1][1]
                        
                        if dealerDisplayString.count('A') >0 and dealerValue+10<=21:
                            dealerace11 = True
                            dealerValue += 10

                        # os.system('cls')
                        # print("Balance: ", round(startingbalance, 1), "\tCards left in the deck: ", len(instance.theDeck), "\tWinrate: ", round(winrate*100,3), "%")
                        # print("===========")
                        # print("Dealer: ",dealerDisplayString )
                        # print("\n\n\n")
                        # print("Your hand: ", yourDisplayString)
                        # print("===========")

                        if dealerValue>21 and dealerace11:
                            dealerace11 = False
                            dealerValue -= 10
                        # print("DealerValue: ",dealerValue)
                        # print("YourValue: ", yourValue)
                        
                        if dealerValue ==21:
                            break

                        
                        if dealerValue>21 and not dealerace11:
                            # print("\nDealer busted!!")
                            iswin = True
                            break
                        # time.sleep(dealingSpeed+1)


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
                    # print("\nCongratulations!! You got BlackJack!")
                if iswin and not blackJack:
                    startingbalance += bet *2
                    # print("\nYou win!")
                if ispush and dealerValue==21:
                    startingbalance += bet
                    # print("\nDealer also got 21! Push!")
                elif ispush:
                    startingbalance += bet
                    # print("\nIt is a push!")
                
                # if not iswin and not isBusted and not ispush:
                #     # print("\nYou lose!")

                # if not isauto:
                #     if iswin:
                #         wait = input("\nPress Enter to collect ur winning and start next round...")
                #     else:
                #         wait = input("\nPress Enter to start next round...")
                # else:
                #     time.sleep(dealingSpeed)
            rreturn.append(startingbalance/10000-1)

            #--------one round end-----------

        # fig, ax = plt.subplots(figsize=(8, 6))

        sumofreturn = 0
        winss = 0
        for i in rreturn:
            sumofreturn += i
            if i >0:
                winss += 1
        ev = sumofreturn/len(rreturn)
        sd = math.sqrt(statistics.pvariance(rreturn))
        sharpe = round(ev/sd, 4)
        gainChance = round(winss/len(rreturn),4)
        listOfSharpe.append(sharpe)
        listOfwinrate.append(gainChance)
        listOfgoalrate.append(goalrate)
        listOfNumofHand.append(numofHands)

        # if listOfwinrate !=[]:
        #     if gainChance > max(listOfwinrate):
        #         maxwinrate = gainChance
        #         maxgoalrate = goalrate
        #         maxnumofhands = numofHands
        #         maxsharpe = sharpe
        #         maxev = round(ev,4)
        #         maxsd = round(sd,4)



        # print("average return: ", sumofreturn/len(rreturn))
        # print("winrate: ", winss/len(rreturn))


        # for i in dictofdifftrial:
        #     ax.plot(i)

        # ax.set_xlabel("number of blackjack hands")
        # ax.set_ylabel("Chips balance")
        # plt.show()

# print(listOfSharpe)
# print(listOfwinrate)


top_10_Sharpe = [listOfSharpe.index(x) for x in sorted(listOfSharpe, reverse=True)[:60]]

print("================")
print("Top 20 sharpe")

for i in range(20):
    print("winrate = ",listOfwinrate[top_10_Sharpe[i]] , ", sharpe = ",listOfSharpe[top_10_Sharpe[i]], ", numofhands = ",listOfNumofHand[top_10_Sharpe[i]])

print("================")
# print("Worst 5 winrate")
# print("winrate = ",listOfwinrate[bottom_5_Winrate[0]] , ", sharpe = ",listOfSharpe[bottom_5_Winrate[0]], ", numofhands = ",listOfNumofHand[bottom_5_Winrate[0]], ", goalrate = ", listOfgoalrate[bottom_5_Winrate[0]])
# print("winrate = ",listOfwinrate[bottom_5_Winrate[1]] , ", sharpe = ",listOfSharpe[bottom_5_Winrate[1]], ", numofhands = ",listOfNumofHand[bottom_5_Winrate[1]], ", goalrate = ", listOfgoalrate[bottom_5_Winrate[1]])
# print("winrate = ",listOfwinrate[bottom_5_Winrate[2]] , ", sharpe = ",listOfSharpe[bottom_5_Winrate[2]], ", numofhands = ",listOfNumofHand[bottom_5_Winrate[2]], ", goalrate = ", listOfgoalrate[bottom_5_Winrate[2]])
# print("winrate = ",listOfwinrate[bottom_5_Winrate[3]] , ", sharpe = ",listOfSharpe[bottom_5_Winrate[3]], ", numofhands = ",listOfNumofHand[bottom_5_Winrate[3]], ", goalrate = ", listOfgoalrate[bottom_5_Winrate[3]])
# print("winrate = ",listOfwinrate[bottom_5_Winrate[4]] , ", sharpe = ",listOfSharpe[bottom_5_Winrate[4]], ", numofhands = ",listOfNumofHand[bottom_5_Winrate[4]], ", goalrate = ", listOfgoalrate[bottom_5_Winrate[4]])
# print("================")
# print("Worst 5 sharpe")
# print("winrate = ",listOfwinrate[bottom_5_Sharpe[0]] , ", sharpe = ",listOfSharpe[bottom_5_Sharpe[0]], ", numofhands = ",listOfNumofHand[bottom_5_Sharpe[0]], ", goalrate = ", listOfgoalrate[bottom_5_Sharpe[0]])
# print("winrate = ",listOfwinrate[bottom_5_Sharpe[1]] , ", sharpe = ",listOfSharpe[bottom_5_Sharpe[1]], ", numofhands = ",listOfNumofHand[bottom_5_Sharpe[1]], ", goalrate = ", listOfgoalrate[bottom_5_Sharpe[1]])
# print("winrate = ",listOfwinrate[bottom_5_Sharpe[2]] , ", sharpe = ",listOfSharpe[bottom_5_Sharpe[2]], ", numofhands = ",listOfNumofHand[bottom_5_Sharpe[2]], ", goalrate = ", listOfgoalrate[bottom_5_Sharpe[2]])
# print("winrate = ",listOfwinrate[bottom_5_Sharpe[3]] , ", sharpe = ",listOfSharpe[bottom_5_Sharpe[3]], ", numofhands = ",listOfNumofHand[bottom_5_Sharpe[3]], ", goalrate = ", listOfgoalrate[bottom_5_Sharpe[3]])
# print("winrate = ",listOfwinrate[bottom_5_Sharpe[4]] , ", sharpe = ",listOfSharpe[bottom_5_Sharpe[4]], ", numofhands = ",listOfNumofHand[bottom_5_Sharpe[4]], ", goalrate = ", listOfgoalrate[bottom_5_Sharpe[4]])











# print("max sharpe is ", maxwinrate)
# print("with a sharpe of ",maxsharpe, ", EV = ", maxev, "sd = ", maxsd)
# print("when numofhand is ", maxnumofhands)
# print("AND goalrate is ", maxgoalrate)

# print(len(listOfSharpe))
# plt.xlim(-0.1,1.2)
# plt.ylim(0.89,0.97)
plt.ylabel('WinRate')
plt.xlabel('Sharpe')
plt.title('Scattered Diagram')
plt.scatter(listOfSharpe, listOfwinrate)
if graph ==1:
    plt.savefig('winrate_vs_sharpe.png')

