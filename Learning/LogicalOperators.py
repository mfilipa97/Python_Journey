#Logical Operators = evaluate multiple conditions ( or, and, not)
#                    or = at least one condition must be True
#                    and = both conditions are True
#                    not = inverts the condition ( not False, not True)
from operator import truediv

#OR
temp = 25
is_raining = False
if temp > 25 or temp < 0 or is_raining:
    print("The outdoor is cancelled")
else:
    print("The outdoor is schedule")

#And and Not

temps = 0
is_sunny = False
if temps >= 28 and is_sunny:
        print("The outdoor is too sunny")
elif temps <0 and is_sunny:
        print("It's Cold Outside and Sunny")
elif temps <= 0 and not is_sunny:
        print("The outdoor is too cold and cloudy")
elif temps >=28 and not is_sunny:
        print("The outdoor is too cold and cloudy")

