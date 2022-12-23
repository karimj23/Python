import random

def deal():
    while len(dealerhand) < 2:
        dealercard = random.randint(1,11)
        dealercard2 = random.randint(1,10)
        dealerhand.append(dealercard)
        dealerhand.append(dealercard2)
        global dealerhandadd
        dealerhandadd = dealerhand[0] + dealerhand[1]
        show = "Dealer showing"
        dealerhandshow = dealerhand[0]
        print (show)
        print (dealerhandshow)

def dealershow():
    if sum(dealerhand) <= 16:
        print("Dealer shows")
        print(sum(dealerhand))
        print("Dealer hits")
        dealercard3 = random.randint(1,11)
        dealerhand.append(dealercard3)
        dealerhandaddhit = sum(dealerhand)
        print(dealerhandaddhit)
        start()
        if dealerhandaddhit > 21:
            print ("Dealer busts, You win!")
            start()
        if dealerhandaddhit <= 16:
            print("Dealer hits")
            dealercard4 = random.randint(1,11)
            dealerhand.append(dealercard4)
            dealerhandaddhit2 = sum(dealerhand)
            if dealerhandaddhit <= 21:
                print("Dealer Shows")
                print(dealerhandaddhit2)
                start()
                if dealerhandaddhit2 > 21:
                    print ("Dealer busts, You win!")
                    start()
    elif sum(dealerhand) >= 16:
        print("Deal shows")
        print(sum(dealerhand))
        start()

def peal():
    while len(playerhand) < 2:
        playercard = random.randint(1,11)
        playercard2 = random.randint(1,10)
        playerhand.append(playercard)
        playerhand.append(playercard2)
        global playerhandadd
        playerhandadd = playerhand[0] + playerhand[1]
        show = "Player has"
        print (show)
        print (playerhand)

def pchoice():
    playerchoice = input("Would you like to hit or stand: ");
    if playerchoice == "hit":
        print("Player hits")
        playercard3 = random.randint(1,11)
        playerhand.append(playercard3)
        playerhandaddhit = sum(playerhand)
        print(playerhandaddhit)
        if playerhandaddhit > 21:
            print ("Player Busts, You Lose!")
            dealershow()
        else:
            pchoice()
    if playerchoice == "stand":
        print("stand")
        dealershow()
    else:
        print("Please type hit or stand")
        pchoice()



#playerchoice2 = input("Would you like to hit or stand: ");

#if playerchoice2 == "hit":
#    playercard4 = random.randint(1,11)
#    playerhand.append(playercard4)
#    playerhandaddhit2 = playerhandadd + playerhand[2] + playerhand[3]
#    if playerhandaddhit < 21:
#        print(playerhandaddhit2)
#        if playerhandaddhit2 > 21:
#            print ("Player Busts, You Lose!")



def start():
    print("***Starting new hand***")
    global dealerhand
    dealerhand = []
    global playerhand
    playerhand = []
    deal()
    peal()
    pchoice()

start()
