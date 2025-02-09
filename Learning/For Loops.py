# for loops =  execute a block of code a fixed number of time
#   You can iterate over a range, string, sequence, tc.

#Count from 1 to 10 RESULT - 1 2 3 4 5 6 7 8 9 10
for counter in range(1,11):
    print(counter)
#Count in reverse enter reversed (range(-) RESULT 10 9 8 7 6 5 4 3 2 1
for reverseCounter in reversed(range(1,11)):
    print(reverseCounter)
print("Happy New Year")

#Count in 2 ( based on what you choose) RESULT 1 3 5 7 9
for counterIn2 in range(1,11, 2): # 2 is the chosen number
    print(counterIn2)

#Skipping a chosen number RESULT 1 2 3 4 5 6 7 8 9 10 11 12 14 until 21
for countTo20 in range (1, 21):
    if countTo20 == 13: #choosen number
        continue
    else:
        print (countTo20)
# When it reached a chosen number it'll stop. RESULT 1 2 3 4 5 6 7 8 9 10 11 12 13 STOP
for countTo20 in range(1, 21):
    if countTo20 == 13: #choosen number
        break
    else:
         print(countTo20)