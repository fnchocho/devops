'''
define a function
use parameters: a, b, c, ...
*arg: we can take unlimited number of positional parameters
*kargs: can take unlimited number of keyword arguments
'''


def add(*args):
    print((type(args)))      
    print(f"The values to add are: {args}")
    s = 0
    for i in args:
        s += i
    print(f"The sum of the values is: {s}.")
    
# call the function 
add(2, 5, 4, 7, 9, 1)    