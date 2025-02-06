import math

#Exercise 1 Calculate circumference of a circle

radius = float (input("Enter radius: "))

circumference = 2 * math.pi * radius

print(f"The circumference is {round (circumference,2)} cm")

#Exercise 2

radius2 = float(input("Enter the radius of circle: "))
area = math.pi * radius2 ** 2

print(f"The area is {round (area,2)} m^2")

#Exercise 3

a = float(input("Enter the A of circle: "))
b = float(input("Enter the B of circle: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The area is {c} m^2")