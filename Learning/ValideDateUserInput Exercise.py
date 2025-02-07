#Validate user input
#1. username can't use more than 12 characters
#2. username can't contain spaces
#3. username must not contain digits

username = input("Enter your username: ")
if len(username) > 12:
    print("Your username is too long. 12 Characters")
elif not username.isalpha():
    print("Your username can't contain numbers")
elif not username.find(" ") == -1:
    print("Your username can't contain space")

else:
    print(f"Your username is {username}")