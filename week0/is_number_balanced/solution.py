def is_number_balanced(n):
	arr = []
	while n != 0:
		arr.append(n % 10)
		n = int(n / 10)
	sum1 = 0
	sum2 = 0
	for i in range(int(len(arr) / 2)):
		sum1 += arr[i]
		sum2 += arr[-(i + 1)]
	return sum1 == sum2
