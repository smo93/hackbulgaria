import sys
from string_utils import tabs_to_spaces

def spacify(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    content = tabs_to_spaces(content, 4)
    outfile = open(filename, 'w')
    outfile.write(content)
    outfile.close()

def main():
    filename = sys.argv[1]
    spacify(filename)

if __name__ == '__main__':
    main()
