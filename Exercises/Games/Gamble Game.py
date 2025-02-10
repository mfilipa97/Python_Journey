import random
import time

def dice():
    total = 120
    game = "Y"
    while game == "Y" or game == "y":
        print("You have = ",total, "Gold")
        bet = int(input("How much do you want to bet? : "))
        while bet > total:
            print("Sorry, you don't have enough money. Please try again.")
            bet = int(input("How much do you want to bet? : "))
            time.sleep(1)
        print(r"""  \_1_/  \_2_/  \_3_/  """)
        guess = int(input("Guess in what bucket the stone is: "))
        while guess > 3:
            print("It is out of 3!!")
            guess = int(input("Guess in what bucket the stone is: "))
        dice1 = random.randint(1, 3)
        print ("It is under bucket number:", dice1)
        if dice1 != guess:
            print("You lose")
            total -= bet
        else:
            print("You win")
            total += bet *2
        if total <= 0:
            input("You don't have more money. Press enter to escape")
            break
        game = input("Do you want to play again? : ")
        game = game.upper()
        if game == "N":
            print ("Thank you for playing. Your total is: ", total, "Gold")

dice()