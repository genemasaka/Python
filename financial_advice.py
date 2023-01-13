ex_rate = 119.50 #variable that stores exchange rate 
months = 12 #variable that stores no. of months 
sal_in_dollars = 123000 #variable that stores salary amount
sal_in_ksh = (ex_rate * sal_in_dollars) / months #equation that calulates monthly sal in ksh
print(f"Your monthly salary in ksh is {sal_in_ksh}") #print string with result of equation formated in
if sal_in_ksh >= 800000: #if statement that prints varied messages depending on salary amount
	print("You are doing well for yourself. Invest your money wisely to retire by 35")
else:
	print("Seek upward mobility in the workplace to increase you chances of retiring by 35")