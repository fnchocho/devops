#Dictionaries are Key:value types
print('\n')
print("Display content of 2 lists to be combined to form a dictionary.")
name = ["Fidel","Odi","Melissa","James"]   # These will parse as values for our dictionary 
profs = ['chemist','nursing','tourism','religion']   # These will parse as values for our dictionary
print(f'We have names = {name}.')
print(f'To combine with these profs = {profs}.\n')
print('To create my_dictionary')

# use the zip function to combine the lists 
my_dictionary = {
key:value for (key,value) in zip(name,profs)
}
print(f'New dictionary = {my_dictionary}.\n')
    
