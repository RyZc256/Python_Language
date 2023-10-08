def main():
    name = input("请输入你的姓名: ")
    length = len(name)
    print("The length of %s is %d" % (name, length))
    PI = 3.14159
    print('%-10.3f' % PI)
    print('%+f' % PI)
    print('%010.3f' % PI)


if __name__ == '__main__':
    main()
