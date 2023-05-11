
def students(**kwargs):
    print(f"The type of data entered is {type}")
    print(f"The keys are: {kwargs.keys}")
    print(kwargs.keys)
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