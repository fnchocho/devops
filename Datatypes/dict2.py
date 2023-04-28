# Modification of exixting library by concatenation
heroes_dict = {
     "Spider": "photographer", 
     "Bat": "philanthropist", 
     "Wonder Wo": "nurse"
 }

heroes_dict = {key+"man":value for (key, value) in heroes_dict.items()}
print(heroes_dict)