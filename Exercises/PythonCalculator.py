operator = input("Please enter your favourite math operator: ")
num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3)) #to round to 3 decimals
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
else:
    print(f"{operator} Invalid operator")