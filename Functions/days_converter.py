num_days = input("Enter the number of day you want to convert to hours: ")
custom_message = input("Type a custome message to print at the end of your run: ")

hours_per_day = 24

def num_hours(num_days, custom_message):
    num_hours = int(num_days) * int(hours_per_day)
    print(f"There are {num_hours} hours in {num_days} days.")
    print(f"{custom_message}!!") 

num_hours(num_days, custom_message)


  
