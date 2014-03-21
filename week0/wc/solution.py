import sys

def main():
    option = sys.argv[1]
    filename = sys.argv[2]
    file = open(filename, "r")
    content = file.read()
    file.close()
    if option.lower() == "chars":
        print(len(content))
    elif option.lower() == "words":
        words = 0
        for line in content.splitlines():
            words += len(line.split())
        print(words)
    elif option.lower() == "lines":
        print(len(content.splitlines()))
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
