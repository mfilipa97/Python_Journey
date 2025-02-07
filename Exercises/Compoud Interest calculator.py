principle = 0
rate = 0
time = 0
# 0 can't be used
while principle <= 0:
    principle = float(input("Enter the principle: "))
    if principle <= 0:
        print("Please enter a positive integer.")

while rate <= 0:
    rate = float(input("Enter the rate: "))
    if rate <= 0:
        print("Please enter a positive integer.")

while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Please enter a positive integer.")
print(principle)
print(rate)
print(time)

total = principle * pow(( 1 + rate /100), time)
print(f"The total is: ${total}")

#To be able to use 0

while True:
    principle = float(input("Enter the principle: "))
    if principle < 0:
        print("Please enter a positive integer.")
    else:
        break

while True:
    rate = float(input("Enter the rate: "))
    if rate < 0:
        print("Please enter a positive integer.")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        print("Please enter a positive integer.")
    else:
        break

print(principle)
print(rate)
print(time)

total = principle * pow(( 1 + rate /100), time)
print(f"The total is: ${total}")