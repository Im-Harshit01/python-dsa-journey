import time

duration = int(input("Enter the time : "))

for x in range(duration, -1, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"\r{hours:02}:{minutes:02}:{seconds:02}", end="")
    if x > 0:
        time.sleep(1)
    
print("Time's over!")
