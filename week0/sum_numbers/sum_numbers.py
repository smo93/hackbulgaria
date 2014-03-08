import sys

def sum_ints_from_file(filename):
	file = open(filename, "r")
	content = file.read()
	ints = content.split()
	result = 0
	for item in ints:
		result += int(item)
	return result

def main():
	filename = sys.argv[1]
	print (sum_ints_from_file(filename))

if __name__ == "__main__":
	main()
