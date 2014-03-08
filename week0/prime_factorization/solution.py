def prime_factorization(n):
	i = 2
	res = []
	while n != 1:
		count = 0;
		if is_prime(i):
			while n % i == 0:
				count += 1
				n /= i
			if count != 0:
				res.append((i, count))
		i += 1
	return res
