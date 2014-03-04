import sys

def concat_files(filenames, target):
    contents = []
    for f in filenames:
        file = open(f, "r")
        contents.append(file.read())
        file.close()
    file = open(target, "w")
    file.write("\n".join(contents))
    file.write("\n")
    file.close()

def main():
    filenames = sys.argv[1:]
    target = "MEGATRON"
    concat_files(filenames, target)

if __name__ == "__main__":
    main()
