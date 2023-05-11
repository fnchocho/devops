'''
define a function
use parameters: a, b, c, ...
'''
def add(a, b, /, c, d, *, e, f):      
    print("I am adding multiple values")
    #formatted (f) string
    print(f"Value of a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, f = {f} ") 
    s =  sum([a,b,c,d,e,f]) 
    return s 

# call the function 
s= add(2, 5, 8, 3, e = 9, f = 1)   #2 and 5 are positional arguments 
print(f"The sum of all the numbers is: {s}")  