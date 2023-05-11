
firt = input("Enter your first name: ")
last = input('Enter your last name: ')

def get_full_name(first, last):
    full_name = first + " " + last
    return full_name  # this value needs to be passed on to a variable

# asign full name to a variable called name and pass arguments for the name to print
name = get_full_name(firt, last)
print(f"Your name is: {name}.")
