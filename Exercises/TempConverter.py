unit = input("Please enter the unit of the temperature you wish to convert (C / F ): ")
temp = float(input("Please enter the temperature you wish to convert: "))

if unit == "C" or unit == "c":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}ºF ")
elif unit == "F" or unit == "f":
    temp = round(( temp - 32) * 5/9, 1)
    print (f"The temp in Celsius is: {temp}ºC")
else:
    print(f"{unit} is not a valid unit")