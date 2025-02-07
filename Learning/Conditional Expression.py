#Conditional Expression =
#           A one-line Shortcut for the if-selse stat
#           Print of assign one of two values based on condition
#           X if condition else Y

num = 5
print ("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

a = 6
b = 7

max_num = a if a > b else b
print(max_num)
min_num = a if a < b else b
print(min_num)

age = 25
status = "Adult" if age >= 18 else "Child"
print(status)

temp = 30
weather = "Warm" if temp >= 23 else "Cloudy"
print(weather)

user_role = "Admin"
access_lvl = "Full Access" if user_role == "Admin" else "Limited Access"
print(access_lvl)
