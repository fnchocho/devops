ls_of_names = ['Fidelis', 'Jane', 'Bine', 'Joel', 'Melissa']
print("Enter the name you want to search: ") 
name_search = input
if name_search in ls_of_names:
    for  name in ls_of_names:
        print(name.upper())
else:
    print("str(name_search) is not found in the list")