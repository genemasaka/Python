high_scores = [1432, 1635, 1345, 2456, 565, 7533, 5321, 2233, 2445]

high_scores.sort(reverse = True)

for top_3_scores in high_scores[:3]:
	print(f'Your highest scores were {top_3_scores}')

for bottom_3_scores in high_scores[6:]:
	print(f'Your lowest scores were {bottom_3_scores}')