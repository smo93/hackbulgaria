def count_consonants(str):
	consonants = 'bcdfghjklmnpqrstvwxz'
	count = 0
	for ch in str:
		if ch in consonants:
			count += 1
	return count 
