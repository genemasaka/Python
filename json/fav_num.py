import json

def store_num():
    name = input('Please enter name:\n')
    num = input('Please enter your favorite number:\n')
    people = []
    num_dict = {name : num}
    people.append(num_dict)
    file_name = 'fav_num.json'
    
    with open(file_name, 'r') as file_object:
        json.dump(people, file_object, indent = 1)
    print(f'Hey, {name.title()} will remember your favorite number is {num}')
    return
store_num()

def get_num():
    file_name = 'fav_num.json'
    with open(file_name, 'r') as fileobj:
       data = json.load(fileobj)
       
       for keys, values in data.items():
           print(f'Hey {keys.title()}, your favorite number is {values}')
    
# get_num()