import sys

def read_file(filename):
	file = open(filename, "r")

	content = file.read()

	file.close()

	return content


def main():
    filename = sys.argv[1]
    print (read_file(filename))

if __name__ == '__main__':
    main()