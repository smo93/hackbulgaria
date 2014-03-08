def list_to_number(digits):
	number = 0
	for dig in digits:
		number = number * 10 + dig
	return number
