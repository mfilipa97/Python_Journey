#nested loops = A loop withing another loop ( outer, inner)
#   outer loop:
#       inner loops:

for repeat in range(3): # repeat the loop counter 3 times
    for counter in range(1,10):
        print(counter, end = " ") # adding end = " " makes the number in 1 line. Putting something else inside adds it.
    print() # add this to make each counter in a new line

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end = "")
    print ()
