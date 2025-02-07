#while loop =  execute some code WHILE some condition remains true

name = input("What is your name? ")
while name == "":
    print("You did not enter a name.")
    name = input("What is your name? ")
else:
    print(f"Hello, {name}")

age = int(input("How old are you? "))

while age <0:
    print("Age cant be negative.")
    age = int(input("How old are you? "))

print(f"You are {age} years old.")

food = input("What is your favourite food?(Q to quit) ")

while not food == "q":
    print(f"You like {food}")
    food = input("What is your other favourite food?(Q to quit) ")

print(f"Bye")

num = int(input("Enter a number between 1-10: "))
while num < 1 or num > 10:
    print(f"{num} is not valid number.")
    num = int(input("Enter a number between 1-10: "))
print (f"{num} is valid number.")