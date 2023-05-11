'''
define a function
use parameters: a, b, c, ...
*arg: we can take unlimited number of positional parameters
**kwargs: can take unlimited number of keyword arguments, this wayy we get a dictionary of arguments
'''
def add(*args):
    print(f"The values to add are: {args}")
    print(f"These values form a {(type(args))}")
    s = 0
    for i in args:
        s += i
    print(f"The sum of the values entered is: {s}")
    
# call the function 
add(2, 5, 4, 7, 9, 1)  

def students(**kwargs):
    print(type(kwargs))
    print(f'The keys are: {(kwargs.keys)}')
    print(f'The values are: {(kwargs.values)}')
    print(f'The keys are: {(kwargs.items)}')

students(name='Fidelis', DOB = '10/28/1994', POB = 'Ohio', Address = '1934 Junction Rd')
