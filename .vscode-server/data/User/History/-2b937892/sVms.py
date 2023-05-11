
def students(**kwargs):
    type = type(students)
    print(f"The type of data entered is {type}")
    keys = kwargs.keys
    print(f"The keys are: {keys}")
    values = kwargs.values
    items = kwargs.items
    print(f"The items are: {items}")

person = {
    'name':'Fidelis', 
    'DOB':'10/28/1994', 
    'POB':'Ohio', 
    'Address':'1934 Junction Rd'
}

students(**person)