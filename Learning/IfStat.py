#if =  do some code if condition is true
#else do something else
from operator import truediv

age = int(input("Enter your age: "))

if age >= 180:
    print("You are too old enough")
elif age < 0:
    print("You are not born yet")
elif age >= 18:
    print("You are old enough")
else:
    print("You are not old enough")

response = input("Would you like food? (Y/N): ")
if response == "Y":
    print("You are food")
else:
    print("You are not food")

name = input("Enter your name: ")
if name == "":
    print("You are not named")
else:
    print(f"You are {name}")

for_sale = True
if for_sale:
    print("You are for sale")
else:
    print("You are not for sale")
