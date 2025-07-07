#1
from datetime import datetime
from dateutil.relativedelta import relativedelta
date=input("Enter your birthday: ")
try:
    birthdate=datetime.strptime(date, "%Y-%m-%d")
    today=datetime.today()
    age=relativedelta(today,birthdate)
    print(f"\nYou are {age.years}years,{age.months}months,{age.days}days old")
except ValueError:
    print("Invalid date format")
#2
from datetime import datetime
date_str = input("Enter your birthdate (YYYY-MM-DD): ")
try:
    birthdate = datetime.strptime(date_str, "%Y-%m-%d")
    today = datetime.today()
    this_year=today.year
    nextBirthday=birthdate.replace(year=this_year)
    if nextBirthday<today:
        nextBirthday=nextBirthday.replace(year=this_year+1)
        days=(nextBirthday-today).days
        print(f"\nThere are {days} days left until your next birthday")
except ValueError:
    print("Invalid date format")
#3
from datetime import datetime, timedelta
currentdate=input("Enter the current date and time: ")
hours=int(input("Enter the duration hours: "))
minutes=int(input("Enter the duration minutes: "))
try:
    current_datetime=datetime.strptime(currentdate,"%Y-%m-%d %H:%M")
    duration =timedelta(hours=hours,minutes=minutes)
    end_time=current_datetime+duration
    print("The meeting will end at:", end_time.strftime("%Y-%m-%d %H:%M"))
except ValueError:
    print("Error:" )
#4
from datetime import datetime
import pytz
try:
    date=input("Enter the date and time(YYYY-MM-DD HH:MM):")
    fromtimezone=input("Enter your current timezone: ")
    totimezone=input("Enter the target timezone: ")
    datetime_obj=datetime.strptime(date, "%Y-%m-%d %H:%M")
    fromtimezone=pytz.timezone(fromtimezone)
    totimezone=pytz.timezone(totimezone)
    localized_datetime = fromtimezone.localize(datetime_obj)
    target_datetime = localized_datetime.astimezone(totimezone)
    print("Converted date and time:", target_datetime.strftime("%Y-%m-%d %H:%M (%Z%z)"))

except Exception as e:
    print("Error:", e)
#5
import time
from datetime import datetime

target = datetime.strptime(input("Enter future date and time (YYYY-MM-DD HH:MM:SS): "), "%Y-%m-%d %H:%M:%S")

while datetime.now() < target:
    diff = target - datetime.now()
    seconds = int(diff.total_seconds())
    print("Time left:", seconds, "seconds", end='\r')
    time.sleep(1)

print("\nTime's up!")

#6
email = input("Enter your email address: ")

if "@" in email and "." in email.split("@")[-1]:
    print("Valid email.")
else:
    print("Invalid email.")
#7
phone = input("Enter 10-digit phone number: ")

formatted = f"({phone[0:3]}) {phone[3:6]}-{phone[6:10]}"
print("Formatted phone number:", formatted)

#8
password = input("Enter your password: ")

if len(password) < 8:
    print("Password too short. Must be at least 8 characters.")
elif not any(c.isupper() for c in password):
    print("Password must contain at least one uppercase letter.")
elif not any(c.islower() for c in password):
    print("Password must contain at least one lowercase letter.")
elif not any(c.isdigit() for c in password):
    print("Password must contain at least one number.")
else:
    print("Password is strong!")

#9
text = """
Python is a powerful programming language. Python is easy to learn.
Many developers love Python because it is versatile and widely used.
"""
word=input("Enter a word to find: ")
words=text.lower().split()
count=words.count(word.lower())
print(f'The word" {word}" was found {count} times')
#10
import re

text = input("Enter your text: ")
pattern = r'\b(?:\d{2}[/-]\d{2}[/-]\d{4}|\d{4}-\d{2}-\d{2})\b'
dates = re.findall(pattern, text)
if dates:
    print("Dates found in the text:")
    for date in dates:
        print("-", date)
else:
    print("No dates found.")
