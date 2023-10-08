def main():
    s = int(input("请输入十进制整数: "))
    f = input("请输入转换进制: ")
    convert = ''
    if f == '2':
        convert = bin(s).replace('0b','')
    elif f == '8':
        convert = oct(s).replace('0o','')
    print(f"十进制数: {s} = ({' '.join(convert)}) {f}进制 ")

if __name__ == '__main__':
    main()