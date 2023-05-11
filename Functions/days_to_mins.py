minutes_per_day = 24*60

def days_to_minutes(num_days):
    return f"\n There are {num_days * minutes_per_day} minutes in {num_days} days. \n"

num_days = input("Enter the number of day you want to convert to hours: ")
if num_days.isdigit() == True:
    num_days = int(num_days)
    if num_days > 0:
       my_minutes = days_to_minutes(num_days)
       print(my_minutes)
    elif num_days == 0:
        print("Zero is not a valid input!")
else:
    print("Your input is not a valid digit, enter a positive digit!")
