import random, sys, time
def intro():
    print("Welcome to Dice of Death!")
    time.sleep(1)
    print("Win and you still live, lose and grim reaper will steal your soul from you")
    time.sleep(1)
    player_name = input("Who are you?")

    if player_name == "" or player_name == " ":
        print("Please enter a name.")
        intro()
        time.sleep(1)
    else:
        print(f"Welcome to Dice of Death,{player_name}!")
        time.sleep(1)
def game(score=0):
    print("Death Rolls first")
    death_roll = random.randint(1, 6)
    print(f"Grim Reaper rolled {death_roll}")
    input("Press Enter to continue...")
    time.sleep(1)
    your_roll = random.randint(1, 15)
    print(f"You rolled {your_roll}")
    input("Press Enter to continue...")
    time.sleep(1)

    if death_roll == your_roll:
        print("You need to play again.")
        game()
    elif death_roll > your_roll:
        print("You lose. And Your life")
        score = 0
    elif your_roll > death_roll:
        print("Guess you were lucky.")
        score += 1
        print(f"Score: {score}")
    play_again = input("Play Again? Yes/No?")
    play_again = play_again.lower() #Returns the string in lower case
    if play_again == "no":
        print("You loser. Press Q to quit.")
        print(f"Score: {score}")
        sys.exit()
    else:
        game(score)
intro()
game()

