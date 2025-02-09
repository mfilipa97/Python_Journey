#Exercise 1:  Write a program that asks the user for a number and prints whether it's odd or even
from encodings import normalize_encoding

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")

#Exercise 2: Grade Calculator - Ask the user for a score (0-100) and print the corresponding grade:
#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: Below 60

score = int(input("Enter a score: "))
if score >= 101:
    print("Your score is higher than 100. Try again.")
    score = int(input("Enter a score: "))
elif (score >= 90) and (score <= 100):
    print(score, "It's an A")
elif (score >= 80) and (score <= 89):
    print(score, "It's a B")
elif (score >= 70) and (score <= 79):
    print(score, "It's a C")
elif (score >= 60) and (score <= 69):
    print(score, "It's a D")
else:
    print(score, "It's a F")

# Exercise 3: Guessing Game
#Write a program that generates a random number between 1 and 10. The user should keep guessing until they get it right.

import random
secret = random.randint(1, 10)
guess = None

while guess != secret:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret:
        print("You guessed right!")
        break
    else:
        print("Guess again!")

#Exercise 4 - Countdown Timer
#Ask the user for a number and count down to 0
import time
num = int(input("Enter a number to countdown from: "))

while num >= 0:
        print(num)
        num -= 1
        time.sleep(1)
print("Counting finished")

# Exercise 5: Multiplication Table
# Ask the user for a number and print its multiplication table up to 10.


num1 = int(input("Enter a number: "))

for i in range(1,11):
    result = num1*i
    print(f"{num1} x {i} = {result}")

#Exercise 6: Sum of Numbers
#Write a program that sums all numbers from 1 to a given number n.

n = int(input("Enter a number: "))
sumOf = 0
for b in range(1, n+1):
    sumOf = sumOf + b
    print(f"The sum of 1 to {n} is {sumOf}")
#WhileLoop Version
c = int(input("Enter a number: "))
sumOf = 0
i = 1
while i <= c:
    sumOf += i
    i += 1
    print(f"The sum of 1 to {n} is {sumOf}")

#. Number Reversal
#Ask the user for a number and print the reverse of that number.
#For example, if the input is 1234, the output should be 4321.

num2 = (input("Enter a number: "))
reversedNumber = ''.join(reversed(num2))
print(f"The reversed number is {reversedNumber}")
