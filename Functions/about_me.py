# This program asks or user inputs, then uses the inputs to display information about the user

name = input ("Enter your first name: ")
profession = input ("Enter your profession: ")
work_place = input ("Enter your work_palce: ")

def about_me(name, profession, work_place):
    print(f"Hi, my name is {name}, I work as {profession} with {work_place}.\n")

about_me(name, profession, work_place)

