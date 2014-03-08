def prime_number_of_divisors(n):
	number_of_divisors = 0
	for i in range(1, n + 1):
		if n % i == 0:
			number_of_divisors += 1
	return is_prime(number_of_divisors)
