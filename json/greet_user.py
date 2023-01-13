import json

file_name = 'username.json'

with open(file_name) as file_object:
    fileobj = json.load(file_object)
    userlist = fileobj.split()
    for user in userlist:
        print(f'Dear {user}, welcome back!')