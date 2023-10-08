def main():
    people = 0
    fraction = []
    while True:
        try:
            people = int(input('请输入评委人数: '))
            if people <= 2:
                print('评委人数异常')
            else:
                break
        except Exception as e:
            print(e)
            pass
    for i in range(people):
        while True:
            try:
                score = float(input(f'请输入第{i+1}个评委的分数: '))
                assert 0 <= score <= 10
                fraction.append(score)
                break
            except:
                print('评委分数有误，重新输入')
    fraction_max = max(fraction)
    fraction_min = min(fraction)
    meanscore = 0
    print('评委原始分'.center(60,'-'))
    print(fraction)
    fraction.remove(fraction_max)
    fraction.remove(fraction_min)
    for i in fraction:
        meanscore = meanscore + i
    meanscore = meanscore / people
    print('去掉最高和最低分'.center(60,'-'))
    print(fraction)
    print('最后得分'.center(60,'-'))
    print(meanscore)



if __name__ == '__main__':
    main()