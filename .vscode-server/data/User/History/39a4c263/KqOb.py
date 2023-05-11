'''
define a function
use parameters: a, b, c, ...
'''
def add(a, b, /, c, d, *, e, f):      
    print("I am adding multiple values")
    #formatted (f) string
    print(f"Value of 
          a = {a}, 
          b= {b}, 
          c = {c},
          d = {d},
          e = {e},
          and f = {f}")  
    
# call the function 
add(2,5)   #2 and 5 are positional arguments  
print(f"The sum of {a} and {b} = {a + b}")   