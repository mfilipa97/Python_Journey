import random
import time

players = ["fox", "hunter", "lord"]

print("This is an alternative game of rock, paper and scissor")
time.sleep(1)
print("")

win_count = 0
lose_count = 0
win = True

while win:
    cpu = random.choice(players)
    user = input("Enter your choice between fox, hunter, lord or exit: ")
    user= user.lower()
    if (user == "fox" and cpu == "lord") or (user == "hunter" and cpu == "fox") or (user == "lord" and cpu == "hunter"):
        print("Computer choose ", cpu)
        print("You choose ", user)
        print("You win!")
        win_count += 1
    elif ( user == "lord" and cpu =="fox") or (user == "fox" and cpu == "hunter") or (user =="hunter" and cpu == "lord"):
        print("Computer choose ", cpu)
        print("You choose ", user)
        print("You lose!")
        lose_count += 1
    elif user == cpu:
        print("Computer choose ", cpu)
        print("You choose ", user)
        print("Everyone survives!")
    elif user == "exit":
        print("Goodbye.")
        print("You won:", win_count, "times." "You lost",lose_count, "times")
        print("Computer won:", lose_count)
        break
    else:
        print("Not a valid choice.")