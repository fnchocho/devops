
personal_data = {
    'name':'Fidelis', 
    'DOB':'10/28/1994', 
    'POB':'Ohio', 
    'Address':'1934 Junction Rd'
}

print(personal_data)
value = personal_data["name"]
print(value)
personal_data["email"] = "negugwa@email.com" #add new key:value pair
print(personal_data) 
del personal_data["DOB"] # delete DOB k:v pair
print(personal_data)

if 'Address' in personal_data:
    print(personal_data["Address"])

try:
    print(personal_data["LastName"])
except:
    print("Error")

#print(personal_data.values())
#print(personal_data.keys())
#print(personal_data.items())

