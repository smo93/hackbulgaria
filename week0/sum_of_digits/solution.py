def sum_of_digits(n):
	s = 0
	while n != 0:
		s += int(n % 10)
		n /= 10
	return s
