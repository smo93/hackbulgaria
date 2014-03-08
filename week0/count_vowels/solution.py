def count_vowels(str):
	vowels = 'aoueiy'
	count = 0
	for ch in str:
		if ch in vowels:
			count += 1
	return count
