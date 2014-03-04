import re
from lesson1 import count_substrings, list_to_number, is_prime

def count_words(arr):
	result = {}
	for word in arr:
		if word in result:
			result[word] += 1
		else:
			result[word] = 1
	return result

def unique_words_count(arr):
	return len(count_words(arr))

def groupby(func, seq):
	result = {}
	for x in seq:
		if func(x) in result:
			result[func(x)].append(x)
		else:
			result[func(x)] = [x]
	return result

def prepare_meal(number):
	count = 0
	while number % 3 == 0:
		count += 1
		number /= 3
	res = ' '.join(["spam"] * count)
	if number % 5 == 0:
		if count > 0:
			res += ' and eggs'
		else:
			res += 'eggs'
	return res

def reduce_file_path(path):
	new_path = re.sub('\w+/\.\./', '/', path)
	new_path = re.sub('/\.\./', '/', new_path)
	new_path = re.sub('\./', '/', new_path)
	new_path = re.sub('//+', '/', new_path)
	if new_path[-1] == '/' and new_path != '/':
		return new_path[:-1]
	return new_path

def is_an_bn(word):
	if len(word) % 2 == 0:
		n = int(len(word) / 2)
		m = re.match('a{'+str(n)+'}b{'+str(n)+'}', word)
		if m == None:
			return False
		else:
			return True
	else:
		return False

def simplify_fraction(fraction):
	i = 2
	while i <= fraction[0]:
		while fraction[0] % i == 0 and fraction[1] % i == 0:
			fraction = (int(fraction[0] / i), int(fraction[1] / i))
		i += 1
	return fraction

def comp_fractions(fr1, fr2):
	f1 = fr1[0] / fr1[1]
	f2 = fr2[0] / fr2[1]
	if f1 < f2:
		return -1
	elif f1 == f2:
		return 0
	else:
		return 1

def sort_fractions(fractions):
	for i in range(len(fractions)):
		min_fr = i
		for j in range(i, len(fractions)):
			if comp_fractions(fractions[j], fractions[min_fr]) == -1:
				min_fr = j
		if i != min_fr:
			tmp = fractions[i]
			fractions[i] = fractions[min_fr]
			fractions[min_fr] = tmp
	return fractions

def nth_fib_lists(listA, listB, n):
	if n == 1:
		return listA
	elif n == 2:
		return listB
	else:
		return nth_fib_lists(listB, listA + listB, n - 1)

def member_of_nth_fib_lists(listA, listB, needle):
	n = 1
	while n < 10:
		nth = nth_fib_lists(listA, listB, n)
		string = str(list_to_number(nth))
		if count_substrings(str(list_to_number(needle)), string):
			return True
		n += 1
	return False

def goldbach(n):
	if n > 2 and n % 2 == 0:
		result = []
		for i in range(2, int(n / 2) + 1):
			if is_prime(i) and is_prime(n - i):
				result.append((i, n - i))
		return result
	else:
		return []

def magic_square(matrix):
	magic_sum = sum(matrix[0])
	transposed = [list(x) for x in zip(*matrix)]
	d1 = [matrix[i][i] for i in range(len(matrix))]
	d2 = [transposed[i][i] for i in range(len(transposed))]
	if sum(d1) != magic_sum and sum(d2) != magic_sum:
		return False
	for row in range(len(matrix)):
		if sum(matrix[row]) != magic_sum or sum(matrix[row]) != magic_sum:
			return False
	return True

def main():
    print (magic_square([[1,2,3], [4,5,6], [7,8,9]]))
    print (magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))

if __name__ == '__main__':
	main()
