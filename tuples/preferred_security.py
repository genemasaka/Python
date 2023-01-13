preferred_security = 'bonds'

if preferred_security != 'stocks':
	print('do not invest in stocks')

pci_stock_highs = [300.34, 232.25, 267.85, 295.45, 303.33]

highest_high = max(pci_stock_highs)
lowest_high  = min(pci_stock_highs)

if highest_high >= 300 and lowest_high >= 250:
	print("Prime Capital's stock hit highs ranging in the 250's to 300's")
else:
	print("Prime Capital stock hit highs ranging in the 200's to 300's")