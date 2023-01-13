def get_formatted_name():
    first = input('Please give me your first name:\n')
    last = input('Please give me your last name:\n')
    formatted_name = f'{first.title()} {last.title()}'
    
    return formatted_name