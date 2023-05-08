import math                 #Top level and entry point of current code

df = math.factorial(3)      # not top level, borrowed, never specified in our console
print("This is a module")   # top level 
print(math.__name__)        # display the name of the top level env where top level code lives 


print('============================================================\n')

def call_me():
    print('Hello Fidel!!')

if __name__ == "__main__":  # condition to import only call me function
    call_me()




