'''
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1.  Ask the user for the number of seconds to set the timer.
2.  Show a live countdown in the terminal.
3.  Notify the user when the timer ends with a final message and **sound (if possible)**.

Bonus:
Format the remaining time as MM:SS.
Use a beep sound (`\a`) at the end if the terminal supports it.
Prevent negative or non-integer inputs.
'''
import time
# for linux
# import winsound

seconds = int(input("Enter the number of seconds: "))

while seconds > 0:
    mins = seconds // 60
    secs = seconds % 60
    time_format = f"{mins:02d}:{secs:02d}"
    print(time_format, end="\r")
    time.sleep(1)
    seconds -= 1

print("Time's up!")
# winsound.Beep(1000, 1000)
