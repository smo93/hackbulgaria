def slope_style_score(scores):
	scores.sort()
	total = 0
	for i in scores[1:-1]:
		total += i
	return total / (len(scores) - 2)
