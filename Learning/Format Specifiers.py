#format specifier = {value:flags} format a value based on what flags are inserter
#   .(number)f = round to that decimal places (fixed point)
#   :(number) = allocate that many spaces
#   :03 = allocate and zero pad that many spaces
#   :< = left justify
#   :> = right justify
#   :^ = center justify
#   :+ = use a plus sign to indicate a positive value
#   := = place a sign to leftmost position
#   : = insert a space before positive numbers
#   :, = comma separator

price1 = 3000.14159
price2 = -987.65
price3 = 12.32
#Decimals
print(f"price1: ${price1:.1f}") #rounding to decimal based on what number you choose
print(f"price2: ${price2:.1f}")
print(f"price3: ${price3:.1f}")

#Spaces
print(f"price1: ${price1:10f}") #creates a space based on what number you choose. If starting with 0 it replaces the spaces with 0 instead
print(f"price2: ${price2:010f}")
print(f"price3: ${price3:5f}")

#Justify to left,right or center < > ^
print(f"price1: ${price1:<10}") # Justify to left
print(f"price2: ${price2:>10}") # Justify to right
print(f"price3: ${price3:^10}") # Justify to center

# + positive value
print(f"price1: ${price1:+}") # Any positive number gives a + sign before
print(f"price2: ${price2:+}") # Since this is a negative number it remains with a -
print(f"price3: ${price3:+}")

#  space for positive number
print(f"price1: ${price1: }") # Any positive number center with other positive number
print(f"price2: ${price2: }") # Since this is a negative number it remains in place
print(f"price3: ${price3: }")

#  , to add commas
print(f"price1: ${price1:,}") # Add a comma when reaching certain numbers
print(f"price2: ${price2:,}")
print(f"price3: ${price3:,}")

#This specifiers can be mixed. Just add one after another