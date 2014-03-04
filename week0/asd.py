def is_an_bn(word):
	count_a = 0
	count_b = 0
	iter = 0
	if word[0] != 'a':
		return False
	else:
		while word[iter] == 'a' and iter <= len(word) - 1:
			count_a = count_a + 1
			iter = iter + 1
		if word[iter] != 'b':
			return False
		else:
			while word[iter] == 'b' and iter <= len(word) - 1:
				count_b = count_b + 1
				iter = iter + 1
	if count_b == count_a and iter == len(word) - 1:
		return True
	else:
		return False