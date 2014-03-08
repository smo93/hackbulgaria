import sys

def read_multiple_files(filenames):
	content = []
	for f in filenames:
		file = open(f, "r")
		content.append(file.read())
		file.close()
	return content


def main():
    print ("\n\n".join(read_multiple_files(sys.argv[1:])))

if __name__ == '__main__':
    main()