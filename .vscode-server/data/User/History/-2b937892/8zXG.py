print(os.getcwd())
def students(**kwargs):
    type = print(type(kwargs))
    keys = print((kwargs.keys))
    values = print((kwargs.values))
    items = print((kwargs.items))

person = {
    'name':'Fidelis', 
    'DOB':'10/28/1994', 
    'POB':'Ohio', 
    'Address':'1934 Junction Rd'
}

students(**person)