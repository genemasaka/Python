trans = ['private jet', 'yatch', 'helicopter', 'maybach s650']

trans[0], trans[1], trans[2] = 'Mercedes Cabriolet', 'Lambo Urus', 'Bently Continental'

print(f'I am going to own a black, fully loaded {trans[3].title()}')
print(f'I regulary fly by {trans[0].title()}. GloJet is my preferred aviation company')
print(f'I am spending my summer on a {trans[1].title()} in the south of France')
print(f'I am buying a {trans[2].title()} so that I can survail my expansive estate')

trans.append('Ferrari 488 Pista')
print(trans)