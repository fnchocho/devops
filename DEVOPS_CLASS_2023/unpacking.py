
def students(**kwargs):
    print(f"The type of data entered is {type}")
    print(f"The keys are: {kwargs.keys}")
    print(students.keys())
    print(f"The items are: {students.items()}")

person = {
    'name':'Fidelis', 
    'DOB':'10/28/1994', 
    'POB':'Ohio', 
    'Address':'1934 Junction Rd'
}

students(person)