greeting = 'Hello Kenya' #created a variable with a string value
if 'World' in greeting:	#if statement to check if 'World' is in greeting 
	print("World is present in greeting")
else:
	print("Word is not present in greeting")

for x in 'eugene': #loop through string ---each char in 'eugene' stored in x and printed to stdout??
	print(x)

name = 'Saucedup' #created varable that stores  a string value
if 'n' in name: #checks char 'n' in name
	print('n is present in name')

NAME = 'eugene' #created variable that stores string value
LASTNAME = 'masaka'# 
print(name !=NAME)#checks if name is not equal to NAME
print(NAME + name)#concantenates string values in NAME and name
for x in name: #loops through chars in name and prints to stdout
	print(x)


print(NAME.upper())#prints string value in NAME in uppercase
print(f"{NAME} {LASTNAME}") #formats string values in NAME and LASTNAME into a single string

message = f'{NAME} {LASTNAME} has to remember to stay calm in this free will experience' #formats values in NAME and LASTNAME into string stored in variable message
print(message.rstrip()) #removes whitespace on the right end of a string
print("Don't")
print(LASTNAME[2:5])