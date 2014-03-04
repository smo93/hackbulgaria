from math import sqrt
def nth_fibonacci(n):
	if n == 1 or n == 2:
		return 1
	return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

def sum_of_digits(n):
	s = 0
	while n != 0:
		s += int(n % 10)
		n /= 10
	return s

def sum_of_min_and_max(arr):
	arr.sort()
	return arr[0] + arr[-1]

def sum_of_divisors(n):
	s = 0
	for i in range(1, n + 1):
		if n % i == 0:
			s += i
	return s

def is_prime(n):
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

def prime_number_of_divisors(n):
	number_of_divisors = 0
	for i in range(1, n + 1):
		if n % i == 0:
			number_of_divisors += 1
	return is_prime(number_of_divisors)

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

def is_int_palindrom(n):
	numb = str(n)
	for i in range(int(len(numb) / 2)):
		if numb[i] != numb[-(i + 1)]:
			return False
	return True

def contains_digit(number, digit):
	str_num = str(number)
	return str(digit) in str_num

def contains_digits(number, digits):
	str_num = str(number)
	for digit in digits:
		if not(str(digit) in str_num):
			return False
	return True

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

def count_substrings(heystack, needle):
	return heystack.count(needle)

def count_vowels(str):
	vowels = 'aoueiy'
	count = 0
	for ch in str:
		if ch in vowels:
			count += 1
	return count

def count_consonants(str):
	consonants = 'bcdfghjklmnpqrstvwxz'
	count = 0
	for ch in str:
		if ch in consonants:
			count += 1
	return count 

def number_to_list(n):
	lst = []
	for ch in str(n):
		lst.append(int(ch))
	return lst

def list_to_number(digits):
	number = 0
	for dig in digits:
		number = number * 10 + dig
	return number

def biggest_difference(arr):
	arr.sort()
	return arr[0] - arr[-1]

def slope_style_score(scores):
	scores.sort()
	total = 0
	for i in scores[1:-1]:
		total += i
	return total / (len(scores) - 2)

def is_increasing(seq):
	for i in range(1, len(seq)):
		if seq[i - 1] >= seq[i]:
			return False
	return True

def is_decreasing(seq):
	for i in range(1, len(seq)):
		if seq[i - 1] <= seq[i]:
			return False
	return True

def what_is_my_sign(day, month):
	signs = {(3, range(21,32)): "Aries", (4, range(1, 21)): "Aries",
		(4, range(21, 31)): "Taurus", (5, range(1, 22)): "Taurus",
		(5, range(22, 31)): "Gemini", (6, range(1, 22)): "Gemini",
		(6, range(22, 32)): "Cancer", (7, range(1, 23)): "Cancer",
		(7, range(23, 32)): "Leo", (8, range(1,23)): "Leo",
		(8, range(23, 31)): "Vigro", (9, range(1,23)): "Vigro",
		(9, range(23, 31)): "Libra", (10, range(1, 23)): "Libra",
		(10, range(23, 32)): "Scorpio", (11, range(1, 22)): "Scorpio",
		(11, range(22, 31)): "Sagittarus", (12, range(1, 22)): "Sagittarus",
		(12, range(22, 32)): "Capricorn", (1, range(1, 20)): "Capricorn",
		(1, range(20, 32)): "Aquarius", (2, range(1, 19)): "Aquarius",
		(2, range(19, 30)): "Pisces", (3, range(1, 21)): "Pisces"}
	for key in signs.keys():
		if month == key[0] and day in key[1]:
			return signs[key]

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

def main():
	lst = [4,1,6,7]
	lst1 = [1,2,3,4,5]
	lst2 = [5,4,3,2,1]
	print (calculate_coins(0.10))
	print (calculate_coins(3.56))

if __name__ == '__main__':
	main()