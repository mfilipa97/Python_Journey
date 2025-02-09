import time

time.sleep(2)
print("You are trying to hack into Armando's email account")
print("                    ")
input("Press enter to continue...")
time.sleep(2)
print("              ")
time.sleep(1)
print("You know that Armando is 56 years old ")
print("               ")
time.sleep(1)
input("Press enter to continue...")
print("Welcome to GMAIL")
time.sleep(2)

correct_password = "nandos1969"
attempt = 0

while True:
    password = input("Enter your password: ").lower()
    attempt += 1

    if password == correct_password:
        print("Access granted")
        print("Welcome Armando")
        break
    else:
        print("Wrong Password")

        if attempt == 1:
            print("Tip: 10 characters are required")
        elif attempt == 3:
            print("Tip: First character 'N'")
        elif attempt == 5:
            print("Tip: Related to his name")
        elif attempt == 7:
            print("Tip: Last three characters are numbers")
        elif attempt == 9:
            print("You're blocked.")
            print("Access denied")
            break

input("Press enter to exit...")