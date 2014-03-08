def calculate_coins(sum):
	coins = [100,50,20,10,5,2,1]
	result = {}
	for coin in coins:
		count = 0
		while sum - coin / 100 >= 0:
			count += 1
			sum -= coin / 100
		result[coin] = count
	return result
