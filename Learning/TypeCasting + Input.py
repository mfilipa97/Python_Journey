#TypeCasting
from operator import itemgetter
from tabnanny import process_tokens

namex = "Mariana" # string
agex = 27 # int
gpax = 3.4 #float
is_student = True #bool
type(namex)
gpax = int(gpax)
agex = str(agex)

#input = A function that prompts the use to enter data and it return as a string

name = input("What is your name?: ")
age = input("How old are you?: ")

age = int(age) # transform the input "string" into int for math
age = age +1

print("Happy Birthday!")
print(f"Hello, {name}!") # use a f string if you want to add variables {_}
print(f"You are {age} years old.")

#Exercise 1 - React Area Calculation

length = float(input ("Enter the length: "))
width= float(input("Enter the width: "))
length = float(length) # This is the equivalent of what is ^
width = float(width)
area = length * width
print(f"The are is: {area} cm")

# Exercise 2 Shopping Cart

item = input ("What item would you like to buy: ")
price = float (input ("What is the price: "))
quantity = int(input ("What is the quantity: "))

total = price * quantity

print(f"The total is: {quantity} x {item}/s")
print(f"Your total is ${total} ")