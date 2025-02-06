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