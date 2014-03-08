def contains_digits(number, digits):
	str_num = str(number)
	for digit in digits:
		if not(str(digit) in str_num):
			return False
	return True
