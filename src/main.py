from time import sleep
from datetime import datetime
from moveMouse import moveMouse

now = str(datetime.now().strftime("%H:%M:%S"))

# Convert datetime (15:00:00) to int 15
currentHour = int(now[0:2])

workStartTime = int(input("Enter work start time (Default is 8): ") or 8)
workEndTime = int(input("Enter work end time (Default is 17): ") or 17)

while(currentHour >= workStartTime and currentHour <= workEndTime):
  sleep(3)
  moveMouse()

print("Work hours are over")