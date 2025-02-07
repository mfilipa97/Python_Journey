#indexing = acessing elements of a sequence using []
#           [ starts : end : step]

credit_number = "1234-4343-5678-6543"

#print(credit_number[4]) # Gives only the 4st number
#print(credit_number[0:4]) # Gives the first 4 numbers
#print(credit_number[5:9]) #From the 5 number till 9
print(credit_number[5:]) # Start -From the 5 number till the end
print(credit_number[-1]) # End -Gives the last number
print(credit_number[::2]) #Step - Skips every 2nd character (jumping every 2 numbers)

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXX-{last_digits}")