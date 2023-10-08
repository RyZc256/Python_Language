def main():
    for i in range(1000):
        sum = 0
        factor = []
        for j in range(1, i+1):
            if (i+1) % j == 0:
                factor.append(j)
                sum = sum + j
        if sum == (i+1):
            print(f'{sum} 是完全数, 真因子为 {factor}')

if __name__ == '__main__':
    main()