import time

my_time = int(input("Enter the time in seconds: "))

for x in reversed(range(0, my_time)):
    # or -> for x in range (my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}") # added :02 to add a 0 before the seconds
    #print(x)
    time.sleep(1) # Use .sleep module to "sleep" for a given amount of time
print("Time's up!")