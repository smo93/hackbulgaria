import sys
from random import randint

def write_integers(filename, n):
	file = open(filename, "w")
	rand_ints = []
	while n != 0:
		rand_ints.append(str(randint(1, 1000)))
		n -= 1
	file.write(" ".join(rand_ints))
	file.write("\n")
	file.close()

def main():
    write_integers(sys.argv[1], int(sys.argv[2]))

if __name__ == '__main__':
    main()