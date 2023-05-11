'''
define a function
use parameters: a, b, c, ...
*arg: we can take unlimited number of positional parameters
*kargs: can take unlimited number of keyword arguments
'''


def add(*args):      
    print(args)
    s = 0
    for i in args:
        s += i
    print(s)
    
# call the function 
add(2, 5, 4, 7, 9, 1)    