def is_int_palindrom(n):
	numb = str(n)
	for i in range(int(len(numb) / 2)):
		if numb[i] != numb[-(i + 1)]:
			return False
	return True
