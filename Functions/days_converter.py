num_days = 1
hours_per_day = 24

def num_hours(num_days, custom_message):
    num_hours = num_days * hours_per_day
    print(f"There are {num_hours} hours in {num_days}.")
    print(f"{custom_message}!!") 

num_hours(5, "Superb" )
