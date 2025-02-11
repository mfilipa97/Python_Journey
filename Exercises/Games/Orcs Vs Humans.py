import time
import random
counter = 0
player_1 = 0
player_2 = 0

def player_1_win():
    print ("Orcs won the battle")
    global player_1 #Uses global to interact with a variable outside the function
    player_1 += 1
def player_2_win():
    print ("Humans won the battle")
    global player_2
    player_2 += 1
while True:
    print ("The war between Orcs vs Humans rage on forever. You are the new commander and you've 1000 men which you have to move to an appropriate position to win the war.")

while True:
    knight = input("How many knight? ")
    try:
        int(knight)
        break
    except:
        print ("This is not a number. Try again.")
while True:
    farmer = input("How many farmers? ")
    try:
        int(farmer)
        break
    except:
        print ("This is not a number. Try again.")
while True:
    defender = input("How many defenders? ")
    try:
        int(defender)
        break
    except:
        print ("This is not a number. Try again.")
tog =int(defender) + int(farmer) +int(knight)
if tog > 1000:
    print("You've moved too many knights, farmer and defenders. Try again.")
else:
    print ("You've", str(defender), "Defenders. You've",str(knight), "knights.And",str(farmer),"farmer")
    break

while True:
    while True:
        counter += 1
        print("The war between Orcs vs Humans rages on forever... and ever")
        time.sleep(1)
        print (". . .")
        time.sleep(1)
        if counter == 3:
            break
print("Someone came out victorious")
x = random.randint(1,3)
time.sleep(x)

defender1 = int(defender) + random.randint(1,15)
farmer1 = int(farmer) + random.randint(1,25)
knight1 = int(knight) + random.randint(1,15)
if defender1 >= 35 and farmer1 >= 15 and knight1 >= 50:
    player_2_win()
else:
    player_1_win()
    print ("Orcs won the battle", +str(player_1)+,"Human victory:" +str(player_2), "knights.")

if player_1 == 5
    print("Orcs won the war")
    break
if player_2 == 5
    print("Humans won the battle")
    break

input("Press Enter to exit")




