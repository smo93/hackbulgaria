def sevens_in_a_row(arr, n):
	count = 0
	for el in arr:
		if el == 7:
			count += 1
		else:
			count = 0
		if count == n:
			return True
	return False
