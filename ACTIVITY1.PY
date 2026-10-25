city = input("ENTER YOUR CITY NAME:")
temp = float(input("ENTER TODAY'S TEMPERATURE IN C:"))

if temp > 35:
    print("WARNING: IT IS VERY HOT TODAY!")

if temp >25:
    print("GREAT DAY TO GO OUTSIDE!")

else:
    print("GRAB A JACKET BEFORE YOU GO OUT!")

if temp >35:
    print("WEATHER: SCORCHING HOT")
elif temp>25:
    print("WEATHER: WARM AND SUNNY")
elif temp>15:
    print("WEATHER: COOL AND BREEZY")
else:
    print("WEATHER: COLD- KEEP WARM")


import datetime
import calendar

now = datetime.datetime.now()
print("CITY:", city)
print("TIME NOW:", now)

print(calendar.calendar(now.year))