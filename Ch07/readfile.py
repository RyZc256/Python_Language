def readfile(filename):
    with open(filename, 'r') as fp:
        all = fp.readlines()
        fp.close()
        for i in all:
            print(i)

def readfile2(filename):
    with open(filename, 'r') as fp:
        text = ""
        for i in fp:
            text = text + i
        print(text)
        fp.close()

def main():
    print("readfile",'\n')
    readfile('password.txt')
    print("readfile2",'\n')
    readfile2('password.txt')

if __name__ == '__main__':
    main()