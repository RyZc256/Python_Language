def main():
    ming = int(input("Please Input Number:  "))
    password = (ming * 10 + 5) / 2 + 3.14159
    print(f'明文{ming}，对应的密文:{password:.3f},取整后:{int(password)}')


if __name__ == '__main__':
    main()
