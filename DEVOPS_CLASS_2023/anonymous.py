# This function can not be immported 

s = lambda a, b: a + b
print(s(6,9))

# Annotations make code more understood to a user
def add(a:int, b:int) -> int:
    return(a + b) 

print(add(3,8))
if __name__ == "__main__":
    add(1,4)