name = input("What is your name? ")
phone = input("What is your phone number? ")

result = len(name) #Lenght of a string and it includes spaces
result_first_find = name.find("a") #First find
result_last_find = name.rfind("a") #Last Find
name = name.capitalize() #Capitalize the first letter
name = name.upper() #Capitalize every letter
name = name.lower() #LoweCase every letter
name = name.isdigit() #True or False if it contains digits ( numbers )
#isAlpha = name.isalpha() #If string contains all alphabetical characters. Spaces don't count so it come out False
phone_number = phone.count("-") # Count how many characters are in a string
phone_num = phone.replace("-", "") #Replace something with another


print(phone_number)
print(phone_num)
print (result)
print (result_first_find)
print (result_last_find)
print (name)
#print (isAlpha)
