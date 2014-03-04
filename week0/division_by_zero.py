def count_numbers(numbers):
	flag = True
	while flag:
		numbers.sort()
		flag = False
		length = len(numbers)
		i = 1
		while i < length:
			A = numbers[i]
			for j in range(i):
				B = numbers[j]
				C = int(A / B)
				if not(C in numbers) and C > 0:
					numbers += [C]
					flag = True
			i += 1
	print (numbers)
	return len(numbers)

def main():
	print (count_numbers([1, 5, 8, 30, 15, 4]))

if __name__ == '__main__':
	main()
