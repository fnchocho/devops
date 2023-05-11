# Create a dictionary
personal_data = {
    'name':'Fidelis', 
    'DOB':'10/28/1994', 
    'POB':'Ohio', 
    'Address':'1934 Junction Rd'
}

# Print parts of the dictionary
print(personal_data)
value = personal_data["name"]
print(value)
print(personal_data.values())
print(personal_data.keys())
print(personal_data.items())

#add new key:value pair
personal_data["email"] = "negugwa@email.com" 
print(personal_data) 

# delete DOB k:v pair
del personal_data["DOB"] 
print(personal_data)

# Loop through a distionary
if 'Address' in personal_data:
    print(personal_data["Address"])

try:
    print(personal_data["LastName"])
except:
    print("Error")               # message to print when exception

# Using for loop 
for key in personal_data:
    print(key)

for values in personal_data.values():
    print(values)


