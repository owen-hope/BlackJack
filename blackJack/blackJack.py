from random import *

def balckJack():
    rand1 = randrange(1, 11)
    total = rand1
    question = input("Your total is " + str(total) + ", do you want to continue? ")
    while question != "No" and question != "no":
        rand1 = randrange(1, 11)
        total += rand1
        if total > 21:
            print("You went over 21 your total is: " + str(total))
            break
        else:
            question = input("Your new Total is " + str(total) + ", do you wish to continue? ")

    rand2 = randrange(1, 11)
    x = randrange(2, 3)
    i = 0
    dealTotal = rand2
    
    while i <= 3:
        dealTotal += rand2
        i += x
    print("The dealer's total is: " + str(dealTotal))

    if dealTotal > 21 and total <= 21:
        return("Congrats, the dealer went over 21, you've won")
    elif dealTotal > 21 and total > 21:
        return("You both went over 21, no winner")
    elif dealTotal == 21 and total == 21:
        return("You and the dealer have tied")
    elif dealTotal <= 21 and total > 21:
        return("Your hand went over 21, the Dealer has won")
    elif dealTotal <= 21 and dealTotal > total:
        return("The daler's hand was closer to 21 than yours. You lose")
    else:
        return("Congrats, you've won, your hand is closer to 21")

print(balckJack())