f = 'text.txt'

try:
    with open(f) as f:
        f.read() 
except FileNotFoundError:
    print(f'{f} does not exist')

   