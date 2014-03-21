from sys import argv
import os


def ext(folder, extension):
    if extension[0] != '.':
        return 0
    if folder[-1] != '/':
        folder += '/'
    if not os.path.isdir(folder):
        return 'No such file or dir: %s' % (folder)
    files = os.listdir(folder)
    files = [f for f in files if f[-len(extension):] == extension]
    return len(files)


def main():
    folder = argv[1]
    extension = argv[2]
    print(ext(folder, extension))

if __name__ == '__main__':
    main()
