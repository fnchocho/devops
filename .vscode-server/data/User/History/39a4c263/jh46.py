'''
define a function
use parameters: a, b, c, ...
'''
def add(a, b, /, c, d, *, e, f):      
    print("I am adding multiple values")
    #formatted (f) string
    print(f"Value of a = {a} and b = {b}") 
    print(f"Value of c = {c} and d = {d}")
    print(f"Value of e = {e} and f = {f}")
      
# call the function 
add(2, 5, 8, 3, e = 9, f = 1)   #2 and 5 are positional arguments 
s =  sum({a},{b})
print(f"The sum of {a} and {b} = {s}")  