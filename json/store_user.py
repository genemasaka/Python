import json

username = input('Please enter name:\n')
f_username = f'{username}\n'
file_name = 'username.json'
active = True
while active:
    with open(file_name, 'a') as file_object:
        json.dump(username, file_object)

    quit = input('Save another user?(yes or no?)\n')
    
    if quit == 'no':
        active = False
print(f'{username} has been saved!')