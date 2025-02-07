# for loops =  execute a block of code a fixed number of time
#   You can iterate over a range, string, sequence, tc.

#Count from 1 to 10
for counter in range(1,11):
    print(counter)
#Count in reverse enter reversed (range(-)
for reverseCounter in reversed(range(1,11)):
    print(reverseCounter)
print("Happy New Year")

#Count in 2 ( based on what you choose)
for counterIn2 in range(1,11, 2): # 2 is the chosen numnber
    print(counterIn2)

#Skipping a chosen number
for countTo20 in range (1, 21):
    if countTo20 == 13: #choosen number
        continue
    else:
        print (countTo20)
# When it reached a chosen number it'll stop.
for countTo20 in range(1, 21):
    if countTo20 == 13: #choosen number
        break
    else:
         print(countTo20)