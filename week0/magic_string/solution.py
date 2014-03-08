def magic_string(string):
	count = 0
	for i in range(int(len(string) / 2)):
		if string[i] != '>':
			string[i] = '>'
			count += 1
	